document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('Form').onsubmit = (event) => {

        document.getElementById('title-errors').innerText = ''
        document.getElementById('description-errors').innerText = ''
        document.getElementById('long-url-errors').innerText = ''


        Title = document.getElementById('title');
        if ( Title.value.length > 100 ){
            event.preventDefault();
            Title.style.borderColor = 'red';
            document.getElementById('title-errors').innerText = 'Title Length Must Be > 0 and <= 100';
        }


        Description = document.getElementById('description');
        if ( Description.value.length > 2000 ){
            event.preventDefault();
            Description.style.borderColor = 'red';
            document.getElementById('description-errors').innerText = 'Description Length Must Be > 0 and <= 2000';
        }


        Long_Url = document.getElementById('long-url');
        if ( Long_Url.value.length > 100 ){
            event.preventDefault();
            Long_Url.style.borderColor = 'red';
            document.getElementById('long-url-errors').innerText = 'Long Url Length Must Be <= 100';
        }
    }

}, false);
