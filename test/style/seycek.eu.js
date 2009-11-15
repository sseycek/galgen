Normal1 = new Image();
Normal1.src = "http://seycek.eu/style/img/Logo_link.png";   
Highlight1 = new Image();
Highlight1.src = "http://seycek.eu/style/img/Logo_hover.png"; 
Highlight2 = new Image();
Highlight2.src = "http://seycek.eu/style/img/Logo_active.png"; 

function Bildwechsel (Bildnr, Bildobjekt)
{window.document.images[Bildnr].src = Bildobjekt.src;}

function metaData(show) {
    var metadata_div = document.getElementById("meta-data-outer");
    if (metadata_div) {
	if (show) metadata_div.style.display="block";
	else metadata_div.style.display="none";
    }
}
