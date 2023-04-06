$(document).ready(function() {
    $('video').each(function() {
        $(this).attr('preload', 'none');
    });
});
