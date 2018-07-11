def create_header(header1, header2, header3, header4):
    return '''
            <tr>
                <th> {} </th>
                <th> {} </th>
                <th> {} </th>
                <th> {} </th>
            </tr>
            '''.format(header1, header2, header3, header4)

# creates row with 4 columns
def create_row(name, location, price, day):
    return '''
            <tr>
                <td> {} </td>
                <td> {} </td>
                <td> {} </td>
                <td> {} </td>
            </tr>
            '''.format(name,location,price,day)


# creates table and sets some CSS.
# note double {{}}. This is to stop {} being seen as reference for .format as values can be added inside for reference to the varibles
# see follwoing for explanation: https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-python-string-and-also-use-fo
def create_table(rows):
    return '''
            <style>
            #fuel {{
                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }}

            #fuel td, #fuel th {{
                border: 1px solid #ddd;
                padding: 8px;
            }}

            #fuel tr:nth-child(even){{background-color: #f2f2f2;}}

            #fuel tr:hover {{background-color: #ddd;}}

            #fuel th {{
                padding-top: 12px;
                padding-bottom: 12px;
                text-align: left;
                background-color: #5DADE2;
                color: white;
            }}
            </style>
            <table id=fuel>
                {}
            </table>
            '''.format(rows)
