function pageStopPropagation(e) {
	if(e.stopPropagation) { e.stopPropagation(); }
	else { e.cancelBubble = true; }
}

var loading_queue = [];
var progress_remain = 0;

function addLoading(id) {
	if (!loading_queue.length) {
		$("#cisco-progress").clearQueue();
		$("#cisco-progress").css("left", 0);
		progress_remain = window.innerWidth;
	}
	loading_queue.push(id);
};

function delLoading(id) {
	setTimeout(function() {
		loading_queue.pop();
		if (loading_queue.length == 0) {
			$("#cisco-progress").animate({left:window.innerWidth*2}, 800);
		}
		else {
			var moving = progress_remain / loading_queue.length
			$("#cisco-progress").animate({left:"+="+moving}, 400);
			progress_remain = progress_remain - moving;
		}
	}, 200);
};

page_preproc = addLoading;
page_postproc = delLoading;
page_errproc = delLoading;

$(document).ready(function() {

	$("#cisco-menu-expander").click(function(e) {
		pageStopPropagation(e);
		$(this).toggleClass("menu_expanded");
		$(".cisco-mainmenu").toggleClass("menu_expanded");
		$(".cisco-init-wrap").toggleClass("menu_expanded");
	});
	
	$(".cisco-sidenav-type-menu").click(function(e) {
		pageStopPropagation(e);
		$(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
	});
	
	$(".cisco-sidenav-type-submenu").click(function(e) {
		pageStopPropagation(e);
		if(!$("#cisco-menu-expander").hasClass("menu_expanded")) {
			var submenu = $("#" + $(this).attr("target_submenu"));
			if (!submenu.hasClass("menu_visible")) {
				$(".cisco-submenu").removeClass("menu_visible");
				submenu.addClass("menu_visible");
				$(".cisco-submenu-closer").addClass("wait_leave");
			} else {
				submenu.removeClass("menu_visible");
				$(".cisco-submenu-closer").removeClass("wait_leave");
			}
		}
	});
	
	$(".cisco-submenu").click(function(e) {
		pageStopPropagation(e);
		$(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
	});
	
	$(".cisco-submenu-closer").mouseenter(function(e) {
		pageStopPropagation(e);
		$(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
	});
	
	$(".cisco-mainmenu-type-submenu").hover(function(e) {
		pageStopPropagation(e);
		$(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
		$(this).find(".cisco-notice-submenu").addClass("cisco-notice-submenu-rotate");
		$(this).find(".cisco-submenu").addClass("menu_visible");
		$(".cisco-submenu-closer").addClass("wait_leave");
	}, function(e) {
		pageStopPropagation(e);
		$(this).find(".cisco-notice-submenu").removeClass("cisco-notice-submenu-rotate");
		$(this).find(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
	});
	
	$(".cisco-topnav-circle").click(function() {
		if($(this).hasClass("cisco-topnav-circle-selected")) {
			$(this).removeClass("cisco-topnav-circle-selected");
		} else {
			$(".cisco-topnav-circle").removeClass("cisco-topnav-circle-selected");
			$(this).addClass("cisco-topnav-circle-selected");
		}
	});

	$("#cisco-topnav-profile").click(function() {
		$(".cisco-profile-wrap").toggleClass("cisco-profile-show");
		$(".cisco-alarm-wrap").removeClass("cisco-alarm-show");
	});

	$("#cisco-topnav-alarm").click(function() {
		$(".cisco-alarm-wrap").toggleClass("cisco-alarm-show");
		$(".cisco-profile-wrap").removeClass("cisco-profile-show");
	});

	$(".cisco-sidenav-menu-info").click(function() {
		$(".cisco-info-page-wrap").toggleClass("cisco-info-show");
		$(".cisco-info").toggleClass("cisco-info-updown");
	});

	$(".cisco-info-page-wrap").click(function() {
		$(this).toggleClass("cisco-info-show");
		$(".cisco-info").toggleClass("cisco-info-updown");
	});
	
});