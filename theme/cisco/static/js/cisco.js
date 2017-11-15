var loading_queue = [];
var progress_remain = 0;
var current_progress = null;

function addLoading(id) {
	if (!loading_queue.length) {
		if (current_progress != null) {
			var progress = $("#" + current_progress);
			progress.clearQueue();
			progress.css("display", "none");
		}
		var vid = create_vid();
		current_progress = vid;
		$("#cisco-progress-wrap").html('<div id="' + vid + '" class="cisco-progress"></div>');
		progress_remain = window.innerWidth;
	}
	loading_queue.push(id);
};

function delLoading(id) {
	setTimeout(function() {
		var moving = progress_remain / loading_queue.length;
		$("#" + current_progress).animate({left:"+="+moving}, 300);
		progress_remain = progress_remain - moving;
		loading_queue.pop();
		if (loading_queue.length == 0) {
			var progress = $("#" + current_progress);
			progress.animate({left:window.innerWidth}, 600);
			progress.fadeOut(600);
		}
	}, 100);
};

page_preproc = addLoading;
page_postproc = delLoading;
page_errproc = delLoading;

$(document).ready(function() {
	
	$(".bootpage-link").unbind("click");
	$(".bootpage-link").click(function() {
		loading_queue = [];
		$(".cisco-sidenav-menu-col").removeClass("cisco-sidenav-menu-col-selected");
		$($(this).attr("sidenav")).addClass("cisco-sidenav-menu-col-selected");
		$("#page_init").attr("page_url", $(this).attr("page_url"));
		page_patch("page_init");
	});
	
	$("#cisco-menu-expander").click(function(e) {
		page_stop_propagation(e);
		$(this).toggleClass("menu_expanded");
		$(".cisco-mainmenu").toggleClass("menu_expanded");
		$(".cisco-init-wrap").toggleClass("menu_expanded");
	});
	
	$(".cisco-sidenav-menu-col").click(function(e) {
		page_stop_propagation(e);
		if ($(this).hasClass("bootpage-link")) {
			$(".cisco-submenu").removeClass("menu_visible");
			$(".cisco-submenu-closer").removeClass("wait_leave");
		} else {
//			if(!$("#cisco-menu-expander").hasClass("menu_expanded")) {
			var submenu = $($(this).attr("submenu"));
			if (!submenu.hasClass("menu_visible")) {
				$(".cisco-submenu").removeClass("menu_visible");
				submenu.addClass("menu_visible");
				$(".cisco-submenu-closer").addClass("wait_leave");
			} else {
				submenu.removeClass("menu_visible");
				$(".cisco-submenu-closer").removeClass("wait_leave");
			}
//			}
		}
	});
	
	$(".cisco-submenu").click(function(e) {
		page_stop_propagation(e);
		$(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
	});
	
	$(".cisco-submenu-closer").mouseenter(function(e) {
		page_stop_propagation(e);
		$(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
	});
	
	$(".cisco-mainmenu-has-submenu").hover(function(e) {
		page_stop_propagation(e);
		$(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
		$(this).find(".cisco-notice-submenu").addClass("cisco-notice-submenu-rotate");
		$(this).find(".cisco-submenu").addClass("menu_visible");
		$(".cisco-submenu-closer").addClass("wait_leave");
	}, function(e) {
		page_stop_propagation(e);
		$(this).find(".cisco-notice-submenu").removeClass("cisco-notice-submenu-rotate");
		$(this).find(".cisco-submenu").removeClass("menu_visible");
		$(".cisco-submenu-closer").removeClass("wait_leave");
	});
	
	$("#cisco-topnav-profile").click(function(e) {
		page_stop_propagation(e);
		$(this).toggleClass("cisco-topnav-circle-selected");
		$(".cisco-profile-wrap").toggleClass("cisco-profile-show");
	});
	
	$("#cisco-topnav-refresh").click(function(e) {
		page_stop_propagation(e);
		page_patch("page_init");
	});
	
	$("#cisco-topnav-refresh").dblclick(function(e) {
		page_stop_propagation(e);
		$(this).toggleClass("cisco-topnav-circle-selected");
	});

	$("#cisco-topnav-alarm").click(function(e) {
		page_stop_propagation(e);
		$(this).toggleClass("cisco-topnav-circle-selected");
		$(".cisco-alarm-wrap").toggleClass("cisco-alarm-show");
	});
	
	$(".cisco-sidenav-info").click(function(e) {
		page_stop_propagation(e);
		$(".cisco-info-page-wrap").toggleClass("cisco-info-show");
		$(".cisco-info").toggleClass("cisco-info-updown");
	});

	$(".cisco-info-page-wrap").click(function(e) {
		page_stop_propagation(e);
		$(this).toggleClass("cisco-info-show");
		$(".cisco-info").toggleClass("cisco-info-updown");
	});
	
});