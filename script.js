console.log("HELLO");
getTrucks();
function getTrucks(){
    console.log("BOOO");
    $.getJSON("271.17.152.34/p4/","Truck",function(data){
	$.each(data,function(i,item){
	    $(".container").append([
		$("<div>")
		.append("<div><img src="+item.picture+"alt=truck style=width:400px; height:400px;></div>")
		]);
	    })
	    });
}
	    
