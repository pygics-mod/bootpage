function datatable_flush_draw(id) {
	var obj = $("#" + id);
	if (preproc != null) { preproc(id); }
	obj.DataTable({
		initComplete: function () { if (postproc != null) { postproc(id); } },
        lengthMenu: [
            [ 10, 25, 50, -1 ],
            [ '10 rows', '25 rows', '50 rows', 'Show all' ]
        ],
        destroy: true
	});
}

function datatable_sync_draw(id) {
	var obj = $("#" + id);
	if (preproc != null) { preproc(id); }
	obj.DataTable({
		ajax: obj.attr("page_url"),
		initComplete: function () { if (postproc != null) { postproc(id); } },
        lengthMenu: [
            [ 10, 25, 50, -1 ],
            [ '10 rows', '25 rows', '50 rows', 'Show all' ]
        ],
        destroy: true
	});
}
