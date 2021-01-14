$(document).ready(function() {
//  creates a variable that captures the path name
    var pathname = window.location.pathname;
// separates the various sections into chunks using '/' to determine where to start the chunk and saves it to a variable (as a list)
    pathSections = pathname.split('/');
// log result to console so I can see if its a list
    consolelog(pathSections)
// if the number of chunks in the path is more than three this means there will be colors added (the first three items are the domain, row numbr and then col number)
    if (pathSections.length > 3) {
// the third item in the pathSections list is the first color added which will be the row color
        var colorOne = pathSection[3];
// the fourth item in the pathSections list is the second color added which will be the col color
        var colorTwo = pathSection[4];
// using jQuery replace the background colors set by the CSS file to the new colors provided
        $('.color1').css('background-color', colorOne);
        $('.color2').css('background-color', colorTwo);
    }
});