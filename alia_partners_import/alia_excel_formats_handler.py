# -*- coding: utf-8 -*-
#
#    Created on 9/05/18
#
#    @authors: alia
#
#
# 2018 ALIA Technologies
#       http://www.alialabs.com
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#


class AliaExcelFormatsHandler:
    """
    
    """
    
    _format_values = [('standard','Standard Basic'),('standardext','Standard Extended'),('camcard','CamCard')]


    def get_excel_supported_formats_list(self):
        """
        :return: list of supported formats
        """
        return self._format_values
    
    
    def get_row(self,type,row):
        """
        :return: list of fields index
        """
        if type == 'standard':
            return self._get_row_standard(row)
        elif type == 'standardext':
            return self._get_row_standardext(row)
        elif type == 'camcard':
            return self._get_row_camcard(row)
        else:
            return None
        
        
    def _get_row_standard(self,row):
        row_dict = {}
        row_dict['ref'] = row[0].value
        row_dict['name'] = row[1].value
        row_dict['vat'] = row[2].value
        row_dict['street'] = row[3].value
        row_dict['city'] = row[4].value
        row_dict['zip'] = row[5].value        
        row_dict['customer'] = True if int(row[6].value) > 0 else False
        row_dict['supplier'] = True if int(row[7].value) > 0 else False
        row_dict['phone'] = False
        row_dict['mobile'] = False
        row_dict['fax'] = False
        row_dict['email'] = False
        row_dict['comercial'] = False
        row_dict['website'] = False
        return row_dict
    
    def _get_row_standardext(self,row):
        row_dict = {}
        row_dict['ref'] = row[0].value
        row_dict['name'] = row[1].value
        row_dict['comercial'] = row[2].value
        row_dict['vat'] = row[3].value
        row_dict['street'] = row[4].value
        row_dict['city'] = row[5].value
        row_dict['zip'] = row[6].value
        row_dict['phone'] = row[7].value
        row_dict['mobile'] = row[8].value
        row_dict['fax'] = row[9].value
        row_dict['email'] = row[10].value
        row_dict['website'] = row[11].value
        row_dict['customer'] = True if int(row[12].value) > 0 else False
        row_dict['supplier'] = True if int(row[13].value) > 0 else False
        return row_dict
    
    def _get_row_camcard(self,row):
        row_dict = {}
        row_dict['ref'] = False
        row_dict['name'] = row[1].value
        row_dict['comercial'] = row[8].value or row[11].value
        row_dict['vat'] = False
        row_dict['street'] = row[29].value or row[30].value
        row_dict['city'] = row[7].value
        row_dict['zip'] = False
        row_dict['phone'] = row[20].value or row[21].value
        row_dict['mobile'] = row[17].value or row[18].value
        row_dict['fax'] = row[23].value or row[24].value
        row_dict['email'] = row[26].value or row[27].value
        row_dict['website'] = row[32].value
        row_dict['customer'] = True
        row_dict['supplier'] = True
        return row_dict
        

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
