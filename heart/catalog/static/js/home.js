window.onload = function(){
	var btn = document.getElementById("check");
	btn.addEventListener("click",function(){
		url = "/catalog/check";
		window.location.replace(url);
	})

	xhr = new XMLHttpRequest ();
	//var cont = document.getElementById("description");
	if(xhr)
	{
		xhr.onreadystatechange = getContent;
		xhr.open("GET", "/catalog/content", true);
		xhr.send(null);
	}
	function getContent(){
		if(xhr.readyState=="4"&&xhr.status==200){
				var cont = document.getElementById("description");
				var data = JSON.parse(xhr.responseText);
				cont.innerHTML = "<br><br><p style='color:white'><font size='4'>"+data['message']+"</font></p>";
				setTimeout(getPic, 4000);
		  }
	}
	function getPic(){
		xhr.open("GET", "/catalog/image", true);
		xhr.onreadystatechange = showImg;
		xhr.send(null);
	}
	function showImg()
	{
		if(xhr.readyState == 4 && xhr.status == 200)
		{
			img = document.getElementById("pic");
			img.src = "data:image/png;base64," + xhr.responseText;
			img.height = 500;
			img.width = 1000;
		}
		setTimeout(getLinks,2000);
	}

	function getLinks()
	{
		xhr.open("GET", "/catalog/link", true);
		xhr.onreadystatechange = showLink;
		xhr.send(null);
	}

	function showLink(){
		if(xhr.readyState==4 && xhr.status==200)
		{
			var data = JSON.parse(xhr.responseText);
			len = Object.keys(data).length;
			htm="<p style='color:white'><font size='5'>Know More:</font></p><br>"
			for(var i=0;i<len;i++)
			{
				htm =htm +"<a href='"+data[i][0]+"'>"+data[i][1]+"</a><br><br>";
			}
			div = document.getElementById('link');
			div.innerHTML = htm;
		}
		setTimeout(getVideo,2000);
	}






	/*function getAudio()
	#{
	#	xhr.open("GET", "/catalog/audio", true);
	#	xhr.onreadystatechange = showaud;
	#	xhr.send(null);
	#}
	#function showaud(){
	#	if(xhr.readyState==4 && xhr.status==200)
	#	{
	#		//console.log(xhr.responseText);
	#		aud = document.getElementById('aud');
	#		aud.src ="data:audio/mp3;base64,"+xhr.responseText; 
	#	}
	#}*/
	
	
	
	
	function getVideo()
	{
		xhr.open("GET", "/catalog/video", true);
		xhr.onreadystatechange = showvid;
		xhr.send(null);
	}
	function showvid(){
		if(xhr.readyState==4 && xhr.status==200)
		{
			//console.log(xhr.responseText);
			vid = document.getElementById('vid');
			vid.src ="data:video/mp4;base64,"+xhr.responseText; 
		}
	}


}
