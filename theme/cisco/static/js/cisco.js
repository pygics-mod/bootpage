function createVid() {
	return 'v-xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
		var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
		return v.toString(16);
	});
}

function pageStopPropagation(e) {
	if(e.stopPropagation) { e.stopPropagation(); }
	else { e.cancelBubble = true; }
}

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
		var vid = createVid();
		current_progress = vid;
		$("#cisco-progress-wrap").html('<div id="' + vid + '" class="cisco-progress"></div>');
		progress_remain = window.innerWidth;
	}
	loading_queue.push(id);
};

function delLoading(id) {
	setTimeout(function() {
		var moving = progress_remain / loading_queue.length;
		console.log('remain', progress_remain, 'moving', moving);
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
		$("#page_init").attr("page_url", $(this).attr("page_url"));
		page_patch("page_init");
	});

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