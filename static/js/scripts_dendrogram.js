$(function() {
	$('#getdendro').click( function() {
		var activeFiles = $('#num_active_files').val();
		if (activeFiles < 2) {
			$("#densubmiterrormessage1").show().fadeOut(1500, "swing");
			return false;
		}
		return true;
	});
});