#!/usr/bin/env python

from xml.etree import cElementTree as etree

default_template = u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">
  <head>
    <title id="title" />
    <meta http-equiv="content-script-type" content="text/javascript" />
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="author" content="Otakar Seycek" />
    <meta name="keywords" lang="de" content="Foto, Fotografie, Reisefotografie, &Ouml;sterreich, Nikon, Portrait, Macro, Makro, Closeup, Close-up, Architektur, Fotograf, Landschaftsfotografie" />
    <meta name="keywords" lang="en-us" content="photo, photograph, photography, travel photography, Austria, Nikon, portrait, macro, closeup, close-up, architecture, landscape photography" />
    <meta name="keywords" lang="en" content="photo, photograph, photography, travel photography, Austria, Nikon, portrait, macro, closeup, close-up, architecture, landscape photography" />
    <link rel="stylesheet" type="text/css" href="res/styles.css" id="css_ref"/>
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
    <td style="width:116px"></td>
    </tr>
    <tr>
<!-- Menu-Zelle -->
    <td>

        <table height="580px" valign="middle" cellspacing="0" cellpadding="0" class="table1">
            <tr>
                <td bgcolor="#111111" style="font-size:11px; font-weight:bold" >
                <p><br /><img src="img/Galerien.png" alt="Galerien" /><br /><br />        
                <a href="reisen.html" id="effect1" class="gal-info" >&nbsp; Reisen</a><br /><br />
                <a href="oesterreich.html" class="gal-info">&nbsp; &Ouml;sterreich</a><br /><br />
                <a href="flora_u_fauna.html" class="gal-info">&nbsp; Flora &amp; Fauna</a><br /><br />

                <a href="landschaften.html" class="gal-info">&nbsp; Landschaften</a><br /><br />
                <a href="menschen.html" class="gal-info">&nbsp; Menschen</a><br /><br />            
                <a href="details.html" class="gal-info">&nbsp; Architektur</a><br /><br />
                <a href="details.html" class="gal-info">&nbsp; Makro &amp; Close-up</a><br /><br />

                <a href="details.html" class="gal-info">&nbsp; P&ecirc;le-m&ecirc;le</a><br /><br />
                <a href="kreativ.html" class="gal-info">&nbsp; Experiment &amp; BW</a><br /><br /><br />
                <img src="img/Info.png" alt="Info" />
                <br /><br />
                <a href="diese_seiten.html" class="gal-info">&nbsp; Diese Seiten</a><br /><br />

                <a href="neues.html" class="gal-info">&nbsp; Neu &amp; aktualisiert</a><br /><br />        
                <a href="kontakt.html" class="gal-info">&nbsp; Kontakt &amp; Impressum</a><br /><br />    
                <a href="vita.html" class="gal-info">&nbsp; Vita</a><br /><br />
                <a href="technik.html" class="gal-info">&nbsp; Meine Technik</a><br /><br />

                <a href="workflow.html" class="gal-info">&nbsp; Mein Workflow</a><br /><br />            
                <a href="blog.html" class="gal-info">&nbsp; Mein Weblog</a><br /><br />
                <a href="gaestebuch.html" class="gal-info">&nbsp; G&auml;stebuch</a></p>        
                <br />
                </td>
            </tr>

        </table>
    </td>

<!-- Haupt-Zelle -->
    <td rowspan="2" bgcolor="#000000" id="content" />
<!-- Thumb-Zelle -->
    <td>
        <table height="580px" width="116" cellspacing="0" cellpadding="0" class="table1">
            <tr><td style="height:80px" align="center" valign="middle"><a href="peyto_lake.html"><img src="navithumbs/Peyto_Lake.jpg" class="navithumb" /></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="robson_river_2.html"><img src="navithumbs/Robson_River_2.jpg" class="navithumb" /></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="kinney_lake.html"><img src="navithumbs/Kinney_Lake.jpg" class="navithumb" /></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="robson_river.html"><img src="navithumbs/Robson_River.jpg" class="navithumb" id="effect2" /></a></td></tr>

            <tr><td style="height:80px" align="center" valign="middle"><a href="dawson_falls.html"><img src="navithumbs/Dawson_Falls.jpg" class="navithumb" /></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="clearwater_lake.html"><img src="navithumbs/Clearwater_Lake.jpg" class="navithumb" /></a></td></tr>
            <tr><td style="height:80px" align="center" valign="middle"><a href="humming_bird.html"><img src="navithumbs/Humming_Bird.jpg" class="navithumb" /></a></td></tr>
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

                    <td style="heigt:38px" align="right" valign="middle"><a href="????.html"><img src="res/prev.png" style="margin-right:2px" class="navi" title="Vorheriges Bild" /></a>
                    </td>
                    <td align="left" valign="middle"><a href="richmond.html"><img src="res/next.png" style="margin-left:2px" class="navi" title="N&auml;chstes Bild" /></a>
                    </td>
                </tr>
                <tr>
                    <td style="heigt:38px" align="right" valign="middle"> <img src="res/info.png" style="margin-right:9px" />
                    </td>

                    <td align="left" valign="middle"><a href="richmond_1.html"><img src="res/full.png" style="margin-left:2px" class="navi" title="Gro&szlig;es Bild" /></a> 
                    </td>
                </tr>
                <tr>
                    <td style="heigt:38px" align="right" valign="middle"><a href="????.html"> <img src="res/slshow.png" style="margin-right:2px" class="navi" title="Slideshow starten" /></a>
                    </td>
                    <td align="left" valign="middle"><a href="kanada.html"><img src="res/index.png" style="margin-left:2px" class="navi" alt="Thumbnail-Seite" title="Thumbnail-Seite" /></a>
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

    def __addXhtmlEntitiesToParser(self, parser):
        parser.entity['nbsp'] = '&#160;'
        parser.entity['iexcl'] = '&#161;'
        parser.entity['cent'] = '&#162;'
        parser.entity['pound'] = '&#163;'
        parser.entity['curren'] = '&#164;'
        parser.entity['yen'] = '&#165;'
        parser.entity['brvbar'] = '&#166;'
        parser.entity['sect'] = '&#167;'
        parser.entity['uml'] = '&#168;'
        parser.entity['copy'] = '&#169;'
        parser.entity['ordf'] = '&#170;'
        parser.entity['laquo'] = '&#171;'
        parser.entity['not'] = '&#172;'
        parser.entity['shy'] = '&#173;'
        parser.entity['reg'] = '&#174;'
        parser.entity['macr'] = '&#175;'
        parser.entity['deg'] = '&#176;'
        parser.entity['plusmn'] = '&#177;'
        parser.entity['sup2'] = '&#178;'
        parser.entity['sup3'] = '&#179;'
        parser.entity['acute'] = '&#180;'
        parser.entity['micro'] = '&#181;'
        parser.entity['para'] = '&#182;'
        parser.entity['middot'] = '&#183;'
        parser.entity['cedil'] = '&#184;'
        parser.entity['sup1'] = '&#185;'
        parser.entity['ordm'] = '&#186;'
        parser.entity['raquo'] = '&#187;'
        parser.entity['frac14'] = '&#188;'
        parser.entity['frac12'] = '&#189;'
        parser.entity['frac34'] = '&#190;'
        parser.entity['iquest'] = '&#191;'
        parser.entity['Agrave'] = '&#192;'
        parser.entity['Aacute'] = '&#193;'
        parser.entity['Acirc'] = '&#194;'
        parser.entity['Atilde'] = '&#195;'
        parser.entity['Auml'] = '&#196;'
        parser.entity['Aring'] = '&#197;'
        parser.entity['AElig'] = '&#198;'
        parser.entity['Ccedil'] = '&#199;'
        parser.entity['Egrave'] = '&#200;'
        parser.entity['Eacute'] = '&#201;'
        parser.entity['Ecirc'] = '&#202;'
        parser.entity['Euml'] = '&#203;'
        parser.entity['Igrave'] = '&#204;'
        parser.entity['Iacute'] = '&#205;'
        parser.entity['Icirc'] = '&#206;'
        parser.entity['Iuml'] = '&#207;'
        parser.entity['ETH'] = '&#208;'
        parser.entity['Ntilde'] = '&#209;'
        parser.entity['Ograve'] = '&#210;'
        parser.entity['Oacute'] = '&#211;'
        parser.entity['Ocirc'] = '&#212;'
        parser.entity['Otilde'] = '&#213;'
        parser.entity['Ouml'] = '&#214;'
        parser.entity['times'] = '&#215;'
        parser.entity['Oslash'] = '&#216;'
        parser.entity['Ugrave'] = '&#217;'
        parser.entity['Uacute'] = '&#218;'
        parser.entity['Ucirc'] = '&#219;'
        parser.entity['Uuml'] = '&#220;'
        parser.entity['Yacute'] = '&#221;'
        parser.entity['THORN'] = '&#222;'
        parser.entity['szlig'] = '&#223;'
        parser.entity['agrave'] = '&#224;'
        parser.entity['aacute'] = '&#225;'
        parser.entity['acirc'] = '&#226;'
        parser.entity['atilde'] = '&#227;'
        parser.entity['auml'] = '&#228;'
        parser.entity['aring'] = '&#229;'
        parser.entity['aelig'] = '&#230;'
        parser.entity['ccedil'] = '&#231;'
        parser.entity['egrave'] = '&#232;'
        parser.entity['eacute'] = '&#233;'
        parser.entity['ecirc'] = '&#234;'
        parser.entity['euml'] = '&#235;'
        parser.entity['igrave'] = '&#236;'
        parser.entity['iacute'] = '&#237;'
        parser.entity['icirc'] = '&#238;'
        parser.entity['iuml'] = '&#239;'
        parser.entity['eth'] = '&#240;'
        parser.entity['ntilde'] = '&#241;'
        parser.entity['ograve'] = '&#242;'
        parser.entity['oacute'] = '&#243;'
        parser.entity['ocirc'] = '&#244;'
        parser.entity['otilde'] = '&#245;'
        parser.entity['ouml'] = '&#246;'
        parser.entity['divide'] = '&#247;'
        parser.entity['oslash'] = '&#248;'
        parser.entity['ugrave'] = '&#249;'
        parser.entity['uacute'] = '&#250;'
        parser.entity['ucirc'] = '&#251;'
        parser.entity['uuml'] = '&#252;'
        parser.entity['yacute'] = '&#253;'
        parser.entity['thorn'] = '&#254;'
        parser.entity['yuml'] = '&#255;'
        parser.entity['lt'] = '&#38;#60;'
        parser.entity['gt'] = '&#62;'
        parser.entity['amp'] = '&#38;#38;'
        parser.entity['apos'] = '&#39;'
        parser.entity['quot'] = '&#34;'
        parser.entity['OElig'] = '&#338;'
        parser.entity['oelig'] = '&#339;'
        parser.entity['Scaron'] = '&#352;'
        parser.entity['scaron'] = '&#353;'
        parser.entity['Yuml'] = '&#376;'
        parser.entity['circ'] = '&#710;'
        parser.entity['tilde'] = '&#732;'
        parser.entity['ensp'] = '&#8194;'
        parser.entity['emsp'] = '&#8195;'
        parser.entity['thinsp'] = '&#8201;'
        parser.entity['zwnj'] = '&#8204;'
        parser.entity['zwj'] = '&#8205;'
        parser.entity['lrm'] = '&#8206;'
        parser.entity['rlm'] = '&#8207;'
        parser.entity['ndash'] = '&#8211;'
        parser.entity['mdash'] = '&#8212;'
        parser.entity['lsquo'] = '&#8216;'
        parser.entity['rsquo'] = '&#8217;'
        parser.entity['sbquo'] = '&#8218;'
        parser.entity['ldquo'] = '&#8220;'
        parser.entity['rdquo'] = '&#8221;'
        parser.entity['bdquo'] = '&#8222;'
        parser.entity['dagger'] = '&#8224;'
        parser.entity['Dagger'] = '&#8225;'
        parser.entity['permil'] = '&#8240;'
        parser.entity['lsaquo'] = '&#8249;'
        parser.entity['rsaquo'] = '&#8250;'
        parser.entity['euro'] = '&#8364;'
            
    def getHTML(self):
        global default_template
        parser = etree.XMLTreeBuilder()
        self.__addXhtmlEntitiesToParser(parser)
        parser.feed(default_template)
        html = parser.close()
        return etree.ElementTree(html)

    HTML = property(getHTML, None)