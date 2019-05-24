function search_table(myInput_id, myTable_id, entries_count_id) {

    var input, pattern, table, tr, td, i, txtValue;
    var j, found;
    var entries_count, span;

    input = document.getElementById(myInput_id);
    pattern = input.value.toUpperCase();
    table = document.getElementById(myTable_id);
    tr = table.getElementsByTagName("tr");

    entries_count = 1;
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        for (j = 0; j < td.length; j++) {
            if (td[j]) {
                txtValue = td[j].textContent || td[j].innerText;
                if (txtValue.toUpperCase().indexOf(pattern) > -1) {
                    found = true;
                    entries_count++;
                    break;
                } else {
                    found = false;
                }
            }
        }
        // Print table head
        if (tr[i].id === "myTableHead") {
            entries_count--;
            found = true;
        }
        // Print table row if pattern was found
        if (found === true) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }

    }
    span = document.getElementById(entries_count_id);
    span.innerText = 'Results: ' + entries_count;
}

function export_table(myTable_id) {
    var html_table = document.getElementById(myTable_id);
    var html = html_table.outerHTML;
    window.open('data:application/vnd.ms-excel,' + encodeURIComponent(html));
}
