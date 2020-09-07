let counter = 0;
function count() {
    counter ++;
    document.querySelector("h1").innerHTML = counter;
    if (counter % 10 == 0) {
        alert(`Count is now ${counter}`);
    }
}

// refer the button AFTER the document is loaded using the listener event
// call the count function (without the ()) when click event happens on the 
// button element.
document.addEventListener('DOMContentLoaded', function() {
    //this works as well:
    //document.querySelector('button').addEventListener('click', count);
    document.querySelector('button').onclick = count;
});
