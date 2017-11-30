# %install_ext http://nicolas.kruchten.com/pivottable/jupyter/pivottablejs.py
# %load_ext pivottablejs
# %pivottablejs data_frame

__version__ = '2.7.0'


template = """
<!DOCTYPE html>
<html>
    <head id="head-pivottable">
        <title>PivotTable.js</title>

        <!-- external libs from cdnjs -->
        <script type="text/javascript">
        var static_url = window.location.href.split('/');
        static_url = static_url.slice(0,6);  // keep up to app 'notebook'
        var staticjs = static_url.join('/');

        var head = document.getElementById('head-pivottable'); // append the scripts to the iframe head
        css_scripts = ["pivot-ajax/c3.min.css", "pivottable/pivot.min.css"];
        for (i = 0; i < css_scripts.length; i++) {
            var link = document.createElement('link');
            link.setAttribute('type', 'text/css');
            link.setAttribute('rel', 'stylesheet');
            var ref = staticjs + '/nbextensions/' + css_scripts[i];
            link.setAttribute('href', ref);
            head.appendChild(link);
        }
        js_scripts = [
                "pivot-ajax/jquery.min.js",    // load jquery first
                "pivot-ajax/jquery-ui.min.js",
                "pivot-ajax/jquery.csv-0.71.min.js",
                "pivot-ajax/d3.min.js",
                "pivot-ajax/c3.min.js",
                "pivottable/pivot.min.js",
                "pivottable/d3_renderers.min.js",
                "pivottable/c3_renderers.min.js",
                "pivottable/export_renderers.min.js"]

        function loadScript() {
            // the js array will be shift until empty
            if (js_scripts.length == 0) {
                userFunction();
                return;
            }
            var static_file = js_scripts.shift()
            var script = document.createElement('script');
            script.setAttribute('type', 'text/javascript');
            var source = staticjs + '/nbextensions/' + static_file; //js_scripts.shift();  //[i];
            script.setAttribute('src', source);
            script.onload = function() {
                loadScript();  // load the scripts synchronously
            }
            head.appendChild(script);
        }
        loadScript();
        </script>
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
        function userFunction() {
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
        }
        </script>
        <div id="output" style="display: none;">%(div)s</div>
    </body>
</html>
"""

from IPython.display import IFrame

def pivot_ui(df, outfile_path = "pivottablejs.html", width="100%", height="500"):
    with open(outfile_path, 'w') as outfile:
        outfile.write(template % {'div': df.to_csv()})
    return IFrame(src=outfile_path, width=width, height=height)
