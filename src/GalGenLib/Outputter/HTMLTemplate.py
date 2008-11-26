#!/usr/bin/env python
# coding=iso-8859-15

from lxml import etree
from lxml.html import XHTMLParser

default_template = '''<?xml version="1.0" encoding="iso-8859-15"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">
  <head>
    <title xml:id="title" />
    <meta http-equiv="content-script-type" content="text/javascript" />
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="author" content="Otakar Seycek" />
    <meta name="keywords" lang="de" content="Foto, Fotografie, Reisefotografie, Österreich, Nikon, Portrait, Macro, Makro, Closeup, Close-up, Architektur, Fotograf, Landschaftsfotografie" />
    <meta name="keywords" lang="en-us" content="photo, photograph, photography, travel photography, Austria, Nikon, portrait, macro, closeup, close-up, architecture, landscape photography" />
    <meta name="keywords" lang="en" content="photo, photograph, photography, travel photography, Austria, Nikon, portrait, macro, closeup, close-up, architecture, landscape photography" />
    <link rel="stylesheet" type="text/css" href="res/styles.css" />
    <script type="text/javascript">
    Normal1 = new Image();
    Normal1.src = "img/Logo_link.png";   
    Highlight1 = new Image();
    Highlight1.src = "img/Logo_hover.png"; 
    Highlight2 = new Image();
    Highlight2.src = "img/Logo_active.png"; 
    function Bildwechsel (Bildnr, Bildobjekt) {
    window.document.images[Bildnr].src = Bildobjekt.src;
    }
    </script>
  </head>
  <body>
    <table cellspacing="0" cellpadding="0" class="table1">

<!-- Logo-Zeile -->
    <tr>
    <td style="width:190px; height:40px"><img src="img/Linse.png" /></td>
    <td style="width:696px"><a href="index.html" onmouseover="Bildwechsel(1, Highlight1)" onclick="Bildwechsel(1, Highlight2)" onmouseout="Bildwechsel(1, Normal1)" title="HOME">
    <img src="img/Logo_link.png" border="0" alt="Home" /></a></td>
    <td style="width:116px" />
    </tr>
    <tr>
<!-- Menu-Zelle -->
    <td>

        <table height="580px" valign="middle" cellspacing="0" cellpadding="0" class="table1">
            <tr>
                <td bgcolor="#111111" style="font-size:11px; font-weight:bold" >
                <p><br /><img src="img/Galerien.png" alt="Galerien"><br /><br />        
                <a href="reisen.html" id="effect1" class="gal-info" >&nbsp; Reisen</a><br /><br />
                <a href="oesterreich.html" class="gal-info">&nbsp; Österreich</a><br /><br />
                <a href="flora_u_fauna.html" class="gal-info">&nbsp; Flora &amp; Fauna</a><br /><br />

                <a href="landschaften.html" class="gal-info">&nbsp; Landschaften</a><br /><br />
                <a href="menschen.html" class="gal-info">&nbsp; Menschen</a><br /><br />            
                <a href="details.html" class="gal-info">&nbsp; Architektur</a><br /><br />
                <a href="details.html" class="gal-info">&nbsp; Makro &amp; Close-up</a><br /><br />

                <a href="details.html" class="gal-info">&nbsp; P&ecirc;le-m&ecirc;le</a><br /><br />
                <a href="kreativ.html" class="gal-info">&nbsp; Experiment &amp; BW</a><br /><br /><br />
                <img src="img/Info.png" alt="Info" >
                <br /><br />
                <a href="diese_seiten.html" class="gal-info">&nbsp; Diese Seiten</a><br /><br />

                <a href="neues.html" class="gal-info">&nbsp; Neu &amp; aktualisiert</a><br /><br />        
                <a href="kontakt.html" class="gal-info">&nbsp; Kontakt &amp; Impressum</a><br /><br />    
                <a href="vita.html" class="gal-info">&nbsp; Vita</a><br /><br />
                <a href="technik.html" class="gal-info">&nbsp; Meine Technik</a><br /><br />

                <a href="workflow.html" class="gal-info">&nbsp; Mein Workflow</a><br /><br />            
                <a href="blog.html" class="gal-info">&nbsp; Mein Weblog</a><br /><br />
                <a href="gaestebuch.html" class="gal-info">&nbsp; Gästebuch</a></p>        
                <br />
                </td>
            </tr>

        </table>
    </td>

<!-- Haupt-Zelle -->
    <td rowspan="2" bgcolor="#000000" xml:id="content" />
<!-- Thumb-Zelle -->
    <td>
        <table height="580px" width="116" cellspacing="0" cellpadding="0" class="table1">
            <tr><td style="height:80px" align="center" valign="middle"><a href="peyto_lake.html"><img src="navithumbs/Peyto_Lake.jpg" class="navithumb"></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="robson_river_2.html"><img src="navithumbs/Robson_River_2.jpg" class="navithumb"></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="kinney_lake.html"><img src="navithumbs/Kinney_Lake.jpg" class="navithumb"></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="robson_river.html"><img src="navithumbs/Robson_River.jpg" class="navithumb" id="effect2"></a></td></tr>

            <tr><td style="height:80px" align="center" valign="middle"><a href="dawson_falls.html"><img src="navithumbs/Dawson_Falls.jpg" class="navithumb"></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="clearwater_lake.html"><img src="navithumbs/Clearwater_Lake.jpg" class="navithumb"></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="humming_bird.html"><img src="navithumbs/Humming_Bird.jpg" class="navithumb"></a></td></tr>
        </table>
    </td>
    </tr>
<!-- Titel-Zelle -->
    <tr>
        <td class="titelzelle">

            <table height="116px" width="190" cellspacing="0" cellpadding="0" class="table1">
                <tr>
                    <td style="height:58px" align="right" valign="bottom"><div class="title">Robson River<br /><br /> </div>
                    </td>
                </tr>
                <tr>
                    <td style="height:58px" align="right" valign="top"><div class="subtitle">Mt Robson National Park<br />Kanada 2007</div>

                    </td>
                </tr>
            </table>
        </td>            
<!-- Navi-Zelle -->
        <td>
            <table width="116" height="116px" cellspacing="0" cellpadding="0" class="table1">
                <colgroup width="58px" span="2"></colgroup>
                <tr>

                    <td style="heigt:38px" align="right" valign="middle"><a href="????.html"><img src="res/prev.png" style="margin-right:2px" class="navi" title="Vorheriges Bild"></a>
                    </td>
                    <td align="left" valign="middle"><a href="richmond.html"><img src="res/next.png" style="margin-left:2px" class="navi" title="Nächstes Bild"></a>
                    </td>
                </tr>
                <tr>
                    <td style="heigt:38px" align="right" valign="middle"> <img src="res/info.png" style="margin-right:9px" >
                    </td>

                    <td align="left" valign="middle"><a href="richmond_1.html"><img src="res/full.png" style="margin-left:2px" class="navi" title="Gro&szlig;es Bild"></a> 
                    </td>
                </tr>
                <tr>
                    <td style="heigt:38px" align="right" valign="middle"><a href="????.html"> <img src="res/slshow.png" style="margin-right:2px" class="navi" title="Slideshow starten"></a>
                    </td>
                    <td align="left" valign="middle"><a href="kanada.html"><img src="res/index.png" style="margin-left:2px" class="navi" alt="Thumbnail-Seite" title="Thumbnail-Seite"></a>
                    </td>
                </tr>

                
            </table>
        </td>    
    </tr>
    </table>
    
  </body>

</html>'''


class HTMLTemplate(object):
    def __init__(self):
        pass

    def getHTML(self):
        global default_template
        parser = XHTMLParser(load_dtd=True)
        html = etree.XML(default_template, parser)
        return html

    HTML = property(getHTML, None)