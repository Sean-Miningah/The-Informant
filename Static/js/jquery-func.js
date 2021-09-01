function navToggleCallback(el)
{
	$(el).toggleClass("minimized");
}

$(document).ready(function(){
	
	$("#sidebar h2").click(function(){
		$(this).next().slideToggle('fast', navToggleCallback(this));
	});
	
	$(".field").focus(function(){
			if($(this).val()==$(this).attr('title'))
				$(this).val("");
		});
	
	$(".field").blur(function(){
			if($(this).val()=="")
				$(this).val($(this).attr('title'));
		});
		
	
	
});