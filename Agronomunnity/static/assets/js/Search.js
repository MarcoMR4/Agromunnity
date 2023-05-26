$(document).ready(function() {
    $('#searchInput').on('keyup', function() {
        var value = $(this).val().toLowerCase();
        $('table tbody tr').each(function() {
            var rowText = $(this).text().toLowerCase();
            $(this).toggle(rowText.indexOf(value) > -1);
        });
    });
});