window.onload = function () {
    $('input').change(function (event) {
        $.ajax({
            url: "/basket/edit/" + event.target.id + "/" + event.target.value,
                
            success: function(data) {
                if (!data.content.delete){
                    $(`.product-${event.target.id}-cost`)[0].innerText = data.content.cost
                    $(`.product-total-cost`)[0].innerText = data.content.total_cost
                } else {
                    $(`.product-${event.target.id}`)[0].innerText = ''
                    $(`.product-total-cost`)[0].innerText = data.content.total_cost
                }
            }
        });
    })
}