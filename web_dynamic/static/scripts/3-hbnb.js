$(document).ready(function() {
    /*
      Amenities selections
     */
    $('.amenities .popover ul li input').click(function() {
        const amenitiesId = [];
        const amenitiesName = [];
        $.each($('.amenities .popover ul li input:checked'), function() {
            amenitiesId.push(this.dataset.id);
            amenitiesName.push(this.dataset.name);
        });
        $('.amenities h4').text(amenitiesName.join(', '));
    });

    /*
      Status API
    */
    $.getJSON('http://0.0.0.0:5001/api/v1/status/', function(data) {
        if (data.status === 'OK') {
            $('header div#api_status').removeClass('not-available').addClass('available');
        }
    });

    /*
     * 4. Fetch places
     */
    const URL = 'http://0.0.0.0:5001/api/v1/places_search/';
    const myData = {};
    $.ajax({
        url: URL,
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(myData),
        success: function(response) {
            $.each(response, function() {
                const temp_view = `
            <article>
              <div class="title_box">
                <h2>` + this.name + `</h2>
                <div class="price_by_night">$` + this.price_by_night + `</div>
              </div>
              <div class="information">
                <div class="max_guest">` + this.max_guest + ` Guest</div>
                <div class="number_rooms">` + this.number_rooms + ` Bedroom</div>
                <div class="number_bathrooms">` + this.number_bathrooms + ` Bathroom</div>
              </div>
              <div class="user">
                <b>Owner:</b> ` + userName(this.user_id) + `
              </div>
              <div class="description">` + this.description + `</div>
            </article>
          `;
                $('section.places').append(temp_view);
            });
        }
    });

    function userName(idUser) {
        let user = '';
        $.ajax({
            url: 'http://0.0.0.0:5001/api/v1/users/' + idUser,
            dataType: 'json',
            async: false,
            success: function(data) {
                user = data.first_name + ' ' + data.last_name;
            }
        });
        return user;
    }
});