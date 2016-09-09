# %install_ext http://nicolas.kruchten.com/pivottable/jupyter/pivottablejs.py
# %load_ext pivottablejs
# %pivottablejs data_frame


template = """
<!DOCTYPE html>
<html>
    <head>
        <title>PivotTable.js</title>

        <!-- external libs from cdnjs -->
        <link rel="stylesheet" type="text/css" href="%(static)s/ajax/c3.min.css">
        <script type="text/javascript" src="%(static)s/pivot-ajax/jquery.min.js"></script>
        <script type="text/javascript" src="%(static)s/pivot-ajax/jquery-ui.min.js"></script>
        <script type="text/javascript" src="%(static)s/pivot-ajax/libs/d3/3.5.5/d3.min.js"></script>
        <script type="text/javascript" src="%(static)s/pivot-ajax/jquery.csv-0.71.min.js"></script>
        <script type="text/javascript" src="%(static)s/pivot-ajax/c3.min.js"></script>

        <link rel="stylesheet" type="text/css" href="%(static)s/pivottable/pivot.min.css">
        <script type="text/javascript" src="%(static)s/pivottable/pivot.min.js"></script>
        <script type="text/javascript" src="%(static)s/pivottable/d3_renderers.min.js"></script>
        <script type="text/javascript" src="%(static)s/pivottable/c3_renderers.min.js"></script>
        <script type="text/javascript" src="%(static)s/pivottable/export_renderers.min.js"></script>

        <style>
            body {font-family: Verdana;}
            .node {
              border: solid 1px white;
              font: 10px sans-serif;
              line-height: 12px;
              overflow: hidden;
              position: absolute;
              text-indent: 2px;
            }
            .c3-line, .c3-focused {stroke-width: 3px !important;}
            .c3-bar {stroke: white !important; stroke-width: 1;}
            .c3 text { font-size: 12px; color: grey;}
            .tick line {stroke: white;}
            .c3-axis path {stroke: grey;}
            .c3-circle { opacity: 1 !important; }
        </style>
    </head>
    <body>
        <script type="text/javascript">
            $(function(){
                if(window.location != window.parent.location)
                    $("<a>", {target:"_blank", href:""})
                        .text("[pop out]").prependTo($("body"));

                $("#output").pivotUI(
                    $.csv.toArrays($("#output").text()),
                    {
                        renderers: $.extend(
                            $.pivotUtilities.renderers,
                            $.pivotUtilities.c3_renderers,
                            $.pivotUtilities.d3_renderers,
                            $.pivotUtilities.export_renderers
                            ),
                        hiddenAttributes: [""]
                    }
                ).show();
             });
        </script>
        <div id="output" style="display: none;">%(div)s</div>
    </body>
</html>
"""

import sys
from IPython.display import IFrame

def pivot_ui(df, outfile_path = "pivottablejs.html", width="100%", height="500"):
    c = get_config()
    print(c.NotebookApp.port)
    static_path = 'http://localhost:%s' % c.NotebookApp.port
    with open(outfile_path, 'w') as outfile:
        outfile.write(template % {'div': df.to_csv(),
                                  'static': '%s/static' % static_path})
    return IFrame(src=outfile_path, width=width, height=height)
