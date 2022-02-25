document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('Form').onsubmit = (event) => {
            
        document.getElementById('title-errors').innerText = '';
        document.getElementById('description-errors').innerText = '';
        document.getElementById('long-url-errors').innerText = '';
        
        
        Title = document.getElementById('title');
        if (Title.value.length > 100 || Title.value.length < 1){
            event.preventDefault();
            Title.style.borderColor = 'red';
            document.getElementById('title-errors').innerText = 'Title Length Must Be > 0 and < 100';
        }
        
        Description = document.getElementById('description');
        if (Description.value.length > 2000 || Description.value.length < 1){
            event.preventDefault();
            Description.style.borderColor = 'red';
            document.getElementById('description-errors').innerText = 'Description Length Must Be > 0 and < 2000';
        }
        
        Long_Url = document.getElementById('long-url');
        if (Long_Url.value.length > 1000 || Long_Url.value.length < 1){
            event.preventDefault();
            Long_Url.style.borderColor = 'red';
            document.getElementById('long-url-errors').innerText = 'Long Url Length Must Be > 0 and < 1000';
        }
    }


    document.getElementById('Delete').onclick = (event) => {

        _Url = event.target.getAttribute('Url');

        _Home = event.target.getAttribute('Home');

        if (!_Url || !_Home){
            return ;
        }

        if (confirm('Are You Sure Want To Delete This Url?')){

            $.ajax(_Url, {

                type: 'DELETE',

                headers: { 
                    "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
                },

                success: function (data, status, xhr) {
                    document.location.href = _Home;
                },

                error: function (jqXhr, textStatus, errorMessage) {
                    console.log(errorMessage);
                    alert('Error Ocurred in Deleting The Url');
                }
            });
        }
    }

}, false);
