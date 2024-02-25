from collections import OrderedDict
from odoo import fields, models, api, _

import io
import base64
import xlsxwriter


class ReportMiningAssetReport(models.AbstractModel):
    _name = 'report.equip3_mining_reports.mining_asset_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'docs': self.env['mining.asset.report'].browse(docids),
            'doc_model': 'mining.asset.report',
        }


class MiningAssetReport(models.TransientModel):
    _name = 'mining.asset.report'
    _description = 'Mining Asset Report'

    @api.model
    def create(self, vals):
        if not vals.get('filter_pit'):
            vals['filter_pit'] = 'all'
        return super(MiningAssetReport, self).create(vals)

    @api.model
    def _get_pit_selection(self):
        selection = [('all', 'All Pits')]
        for pit in self.env['mining.project.control'].search([]):
            pit_area = pit.facilities_area_id and pit.facilities_area_id.display_name or 'False'
            selection += [(str(pit.id), '%s (%s)' % (pit.display_name, pit_area))]
        return selection

    filter_pit = fields.Selection(
        selection=_get_pit_selection,
        string='Filter Pit',
        default='all'
    )
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    def get_report_values(self):
        return {
            'filters': self.get_filters(),
            'data': self.get_asset_values()
        }

    def get_filters(self):
        selection = self.fields_get(allfields=['filter_pit'])['filter_pit']['selection']
        return {
            'filter_pit': {
                'selection': selection,
                'active': (self.filter_pit, dict(selection).get(self.filter_pit, 'All Pits'))
            }
        }

    def get_asset_values(self):

        def _parse(objs):
            product_ids = sorted(set(objs.mapped('product_id')), key=lambda o: o.id)
            values = []
            for product_id in product_ids:
                objs_product = objs.filtered(lambda o: o.product_id == product_id)
                try:
                    qty = sum(objs_product.mapped('qty_done'))
                except KeyError:
                    qty = sum(objs_product.mapped('total_amount'))
                values += [{
                    'id': product_id.id,
                    'name': product_id.display_name,
                    'model': product_id._name,
                    'description': product_id._description,
                    'uom': product_id.uom_id.name,
                    'qty': qty
                }]
            return values

        def _prepare(obj, assets, inputs, outputs, fuels, deliveries):
            output_ids = _parse(outputs)
            delivery_ids = _parse(deliveries)

            for delivery in delivery_ids:
                found = False
                for o, output in enumerate(output_ids):
                    if delivery['id'] == output['id']:
                        found = True
                        break
                if found:
                    output_ids[o]['qty'] += delivery['qty']
                else:
                    output_ids += [delivery]

            return {
                'id': obj.id,
                'name': obj.display_name,
                'model': obj._name,
                'description': obj._description,
                'input_ids': _parse(inputs),
                'output_ids': output_ids,
                'fuel_ids': _parse(fuels),
                'duration': sum(assets.mapped('duration')),
                'children': []
            }

        asset_domain = []
        act_domain = [('state', '=', 'confirm')]
        if self.filter_pit != 'all':
            pit_id = self.env['mining.project.control'].browse(int(self.filter_pit))
            asset_domain += [('fac_area', '=', pit_id.facilities_area_id.id)]
            act_domain += [('mining_project_id', '=', pit_id.id)]

        asset_ids = self.env['maintenance.equipment'].search(asset_domain)
        operation_ids = self.env['mining.operations.two'].search([])
        act_ids = self.env['mining.production.actualization'].search(act_domain)

        act_asset_ids = act_ids.mapped('assets_ids')
        act_input_ids = act_ids.mapped('input_ids')
        act_output_ids = act_ids.mapped('output_ids')
        act_fuel_ids = act_ids.mapped('fuel_ids')
        act_delivery_ids = act_ids.mapped('delivery_ids')

        data = {'children': []}
        for asset in asset_ids:
            asset_asset_ids = act_asset_ids.filtered(lambda i: i.assets_id == asset)
            asset_input_ids = act_input_ids.filtered(lambda i: i.asset_id == asset)
            asset_output_ids = act_output_ids.filtered(lambda o: o.asset_id == asset)
            asset_fuel_ids = act_fuel_ids.filtered(lambda f: f.asset_id == asset)
            asset_delivery_ids = act_delivery_ids.filtered(lambda d: d.asset_id == asset)
            asset_values = _prepare(asset, asset_asset_ids, asset_input_ids, asset_output_ids, asset_fuel_ids,
                                    asset_delivery_ids)

            for operation in operation_ids:
                operation_asset_ids = asset_asset_ids.filtered(lambda i: i.operation_id == operation)
                operation_input_ids = asset_input_ids.filtered(lambda i: i.operation_id == operation)
                operation_output_ids = asset_output_ids.filtered(lambda o: o.operation_id == operation)
                operation_fuel_ids = asset_fuel_ids.filtered(lambda f: f.operation_id == operation)
                operation_delivery_ids = asset_delivery_ids.filtered(lambda d: d.operation_id == operation)
                operation_values = _prepare(operation, operation_asset_ids, operation_input_ids, operation_output_ids,
                                            operation_fuel_ids, operation_delivery_ids)

                record_ids = sorted(set(
                    operation_input_ids.mapped('mining_prod_act_id') | \
                    operation_output_ids.mapped('mining_prod_act_id') | \
                    operation_fuel_ids.mapped('mining_prod_act_id') | \
                    operation_delivery_ids.mapped('mining_prod_act_id')
                ), key=lambda r: r.id)

                for record in record_ids:
                    record_asset_ids = operation_asset_ids.filtered(lambda i: i.mining_prod_act_id == record)
                    record_input_ids = operation_input_ids.filtered(lambda i: i.mining_prod_act_id == record)
                    record_output_ids = operation_output_ids.filtered(lambda o: o.mining_prod_act_id == record)
                    record_fuel_ids = operation_fuel_ids.filtered(lambda f: f.mining_prod_act_id == record)
                    record_delivery_ids = operation_delivery_ids.filtered(lambda d: d.mining_prod_act_id == record)
                    record_values = _prepare(record, record_asset_ids, record_input_ids, record_output_ids,
                                             record_fuel_ids, record_delivery_ids)

                    if record_fuel_ids:
                        for fuel in record_fuel_ids:
                            fuel_values = _prepare(record, record_asset_ids, record_input_ids, record_output_ids, fuel,
                                                   record_delivery_ids)
                            record_values['children'] += [fuel_values]
                    else:
                        record_values['children'] += [
                            _prepare(record, record_asset_ids, record_input_ids, record_output_ids, record_fuel_ids,
                                     record_delivery_ids)]

                    operation_values['children'] += [record_values]
                asset_values['children'] += [operation_values]
            data['children'] += [asset_values]
        return data

    def print_xlsx_report(self):
        file_name = 'Asset Production Report.xlsx'

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        title_format = workbook.add_format({
            'bold': 1,
            'font_size': 15
        })

        subtitle_format = workbook.add_format({
            'bold': 1,
            'font_size': 13
        })

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
        })

        subheader_format = workbook.add_format({
            'border': 1,
            'bg_color': '#dee2e6',
        })

        bordered = workbook.add_format({
            'border': 1
        })

        data = self.get_asset_values()

        header = ['', 'Product/Input', 'Input', 'UoM', 'Product/Output', 'Output', 'UoM', 'Duration', 'Fuel Type',
                  'Fuel Usage', 'UoM']

        width = []
        for head in header:
            width.append(len(head) + 2)

        row = 1
        worksheet.write(row, 0, '%s: %s' % (self.company_id.name, _('Asset Production Report')), title_format)

        row += 2
        worksheet.write(row, 0, 'Pit', subtitle_format)
        worksheet.write(row, 1, ': %s' % dict(self._get_pit_selection()).get(self.filter_pit, 'All Pits'),
                        subtitle_format)

        row += 1
        for asset in data['children']:

            # if asset['name'] == 'Caterpillar 320D Hydraulic Excavator [CAT 320 D1]':
            #     print('the asset is : ', asset)
                row += 1
                for col, head in enumerate([asset['name']] + header[1:]):
                    #column 1 NONE
                    worksheet.write(row, col, head, header_format)

                row += 1
                for operation in asset['children']: #mineral
                    
                    # column 1 NONE
                    worksheet.write(row, 0, operation['name'], subheader_format)
                    width[0] = max((width[0], len(str(operation['name'])) + 2))

                    # COLUMN 2 PRODUCT INPUT
                    if operation['input_ids']:
                        input_names = [input['name'] for input in operation['input_ids']]
                        input_names_str = ', '.join(input_names)
                        worksheet.write(row, 1, input_names_str, subheader_format)
                        width[0] = max((width[0], len(str(input_names_str)) + 2))
                        input_ids_str = ', '.join(map(str, operation['input_ids']))
                    # COLUMN 3 INPUT
                        input_qty = [input['qty'] for input in operation['input_ids']]
                        input_qty_str = ', '.join(str(input_qty) for qty in input_qty)
                        worksheet.write(row, 2, input_qty_str, subheader_format)
                        width[0] = max((width[0], len(str(input_qty_str)) + 2))
                        col = 3
                    #COLUMN 4 UOM
                        uom = operation['input_ids'][0].get('uom')
                        worksheet.write(row, col, uom, subheader_format)
                        width[col] = max((width[col], len(str(uom)) + 2))
                    else:
                        worksheet.write(row, col, None, subheader_format)
            
                    col = 4
                    #COLUMN 5 PRODUCT/OUTPUT``
                    if operation['output_ids']:
                        output_names = [output['name'] for output in operation['output_ids']]
                        output_names_str = ', '.join(output_names)
                        worksheet.write(row, col, output_names_str, subheader_format)
                        width[col] = max((width[col], len(str(output_names_str)) + 2))
                    # COLUMN 6 OUTPUT
                        col = 5
                        output_qty = [output['qty'] for output in operation['output_ids']]
                        output_qty_str = ', '.join(str(qty) for qty in output_qty)
                        worksheet.write(row, col, output_qty_str, subheader_format)
                        width[col] = max((width[col], len(str('')) + 2))
                    # COLUMN 7 UOM
                        output_uom = [output['uom'] for output in operation['output_ids']]
                        output_uom_str = ', '.join(output_uom)
                        worksheet.write(row, 6, output_uom_str, subheader_format)

                    else:
                        worksheet.write(row, 4, None, subheader_format)
                        worksheet.write(row, 5, None, subheader_format)
                        worksheet.write(row, 6, None, subheader_format)
                    
                    # COLUMN 8 DURATION
                    if operation['duration'] :
                        worksheet.write(row, 7, operation['duration'], subheader_format)
                        width[col] = max((width[col], len(str(operation['duration'])) + 2))
                    else :
                        worksheet.write(row, 7, None, subheader_format)
                
                    if operation['fuel_ids']:
                        # COLUMN 9 FUEL TYPE
                        fuel_names = [fuel['name'] for fuel in operation['fuel_ids']]
                        fuel_names_str = ', '.join(fuel_names)
                        worksheet.write(row, 8, fuel_names_str, subheader_format)
                         # COLUMN 10 FUEL USAGE
                        fuel_qty = [fuel['qty'] for fuel in operation['fuel_ids']]
                        fuel_qty_str = ', '.join(str(qty) for qty in fuel_qty)

                        # fuel_qty_str = ', '.join(fuel_qty)
                        worksheet.write(row, 9, fuel_qty_str, subheader_format)
                        # COLUMN 11 UOM
                        fuel_uom = [fuel['uom'] for fuel in operation['fuel_ids']]
                        fuel_uom_str = ', '.join(fuel_uom)
                        worksheet.write(row, 10, fuel_uom_str, subheader_format)
                    else:
                        worksheet.write(row, 8, None, subheader_format)
                        worksheet.write(row, 9, None, subheader_format)
                        worksheet.write(row, 10, None, subheader_format)

                    row += 1

                for record in operation['children']:
                    for fuel in record['children']:

                        #COLUMN 1 NAME
                        fuel_name = '    %s' % fuel['name']
                        worksheet.write(row, 0, fuel_name, bordered)
                        width[0] = max((width[0], len(str(fuel_name)) + 2))
                        if fuel['input_ids']:
                            # COLUMN 2 PRODUCT INPUT
                            input_names = [input['name'] for input in fuel['input_ids']]
                            input_names_str = ', '.join(input_names)
                            worksheet.write(row, 1, input_names_str, subheader_format)
                            width[0] = max((width[0], len(str(input_ids_str)) + 2))
                            # COLUMN 3 INPUT
                            input_qty = [input['qty'] for input in operation['input_ids']]
                            input_qty_str = ', '.join(str(qty) for qty in input_qty)
                            worksheet.write(row, 2, input_qty_str, subheader_format)
                            width[0] = max((width[0], len(str(input_qty_str)) + 2))
                            # COLUMN 4 UOM INPUT
                            uom = fuel['input_ids'][0].get('uom')
                            worksheet.write(row, 3, uom, subheader_format)
                            width[col] = max((width[col], len(str(uom)) + 2))
                        else:
                            worksheet.write(row, 3, None, subheader_format)
                            width[col] = max((width[col], len(str('')) + 2))
                        
                        # COLUMN 5 PRODUCT NAME OUTPUT
                        if fuel['output_ids']:
                            output_names = [output['name'] for output in fuel['output_ids']]
                            output_names_str = ', '.join(output_names)
                            worksheet.write(row, 4, output_names_str, subheader_format)
                            width[col] = max((width[col], len(str(output_names_str)) + 2))
                                # COLUMN 6 OUTPUT
                            col = 5
                            output_qty = [output['qty'] for output in fuel['output_ids']]
                            output_qty_str = ', '.join(str(qty) for qty in output_qty)
                            worksheet.write(row, col, output_qty_str, subheader_format)
                            width[col] = max((width[col], len(str('')) + 2))
                            # COLUMN 7 UOM
                            output_uom = [output['uom'] for output in fuel['output_ids']]
                            output_uom_str = ', '.join(output_uom)
                            worksheet.write(row, 6, output_uom_str, subheader_format)
                        else:
                            worksheet.write(row, 4, None, subheader_format)
                            worksheet.write(row, 5, None, subheader_format)
                            worksheet.write(row, 6, None, subheader_format)
                            
                            # COLUMN 8 DURATION
                        if fuel['duration']:
                            worksheet.write(row, 7, fuel['duration'], subheader_format)
                            width[col] = max((width[col], len(str(operation['duration'])) + 2))
                        else:
                            worksheet.write(row, 7, None, subheader_format)
                        
                        if fuel['fuel_ids']:
                            # COLUMN 9 FUEL TYPE
                            fuel_names = [fuel['name'] for fuel in fuel['fuel_ids']]
                            fuel_names_str = ', '.join(fuel_names)
                            worksheet.write(row, 8, fuel_names_str, subheader_format)
                            # COLUMN 10 FUEL USAGE
                            fuel_qty = [fuel['qty'] for fuel in fuel['fuel_ids']]
                            fuel_qty_str = ', '.join(str(qty) for qty in fuel_qty)
                            # fuel_qty_str = ', '.join(fuel_qty)
                            worksheet.write(row, 9, fuel_qty_str, subheader_format)
                            # COLUMN 11 UOM
                            fuel_uom = [fuel['uom'] for fuel in fuel['fuel_ids']]
                            fuel_uom_str = ', '.join(fuel_uom)
                            worksheet.write(row, 10, fuel_uom_str, subheader_format)
                        else:
                            worksheet.write(row, 8, None, subheader_format)
                            worksheet.write(row, 9, None, subheader_format)
                            worksheet.write(row, 10, None, subheader_format)
                        row += 1

        for col, w in enumerate(width):
            worksheet.set_column(col, col, w)

        workbook.close()

        output.seek(0)
        result = base64.b64encode(output.read())
        attachment_id = self.env['ir.attachment'].create({'name': file_name, 'store_fname': file_name, 'datas': result})
        output.close()
        return attachment_id.id
