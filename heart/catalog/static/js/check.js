window.onload = function(){
	var sub = document.getElementById("sub");
	sub.addEventListener("click",function(){
		var age = document.getElementById('age').value;
		var loc = document.getElementById('loc').value;
		var gen = document.getElementById('gender').value;
		var cpt = document.getElementById('cpt').value;
		var rbp = document.getElementById('rbp').value;
		var chol = document.getElementById('chol').value;
		var fbs = document.getElementById('fbs').value;
		var recg = document.getElementById('recg').value;
		var mhr = document.getElementById('mhra').value;
		var eia = document.getElementById('eia').value;
		var st = document.getElementById('st').value;
		var thal = document.getElementById('thal').value;
		var slope = document.getElementById('slope').value;
		var cv = document.getElementById('cv').value;
		url = '/catalog/predict?age='+age+'&loc='+loc+'&gen='+gen+'&cpt='+cpt+'&rbp='+rbp+'&chol='+chol+'&fbs='+fbs+'&recg='+recg+'&mhr='+mhr+'&eia='+eia+'&st='+st+'&thal='+thal+'&slope='+slope+'&cv='+cv;
		window.location.replace(url);
		console.log(url);
	});
}