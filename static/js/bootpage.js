$(document).ready(function(){
	$(".bootpage-link").click(function() {
		$("#page_init").attr("page_url", $(this).attr("page_url"));
		page_patch("page_init");
	});
});