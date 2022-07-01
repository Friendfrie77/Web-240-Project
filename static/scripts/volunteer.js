/* show and hide calander */
jQuery(function() {
    jQuery('.job-image').click(function() {
      jQuery('#job'+$(this).attr('target')).slideToggle();
    });
});

function ShowCalendar1() {
  var calendarEl = document.getElementById('calendar1');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    googleCalendarApiKey: 'AIzaSyBvT8Tqbh0ygPsWTylTiE0MejzwDsr9bQU',
    events: {
      googleCalendarId: 'k8h6u4seguf3d3ilm7gle4hhpo@group.calendar.google.com'
    }
  });
  calendar.render();
};
function ShowCalendar2() {
  var calendarEl = document.getElementById('calendar2');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    googleCalendarApiKey: 'AIzaSyBvT8Tqbh0ygPsWTylTiE0MejzwDsr9bQU',
    events: {
      googleCalendarId: '28ssr4sdgptg56f5evch02n9t4@group.calendar.google.com'
    }
  });
  calendar.render();
};
function ShowCalendar3() {
  var calendarEl = document.getElementById('calendar3');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    googleCalendarApiKey: 'AIzaSyBvT8Tqbh0ygPsWTylTiE0MejzwDsr9bQU',
    events: {
      googleCalendarId: '28ssr4sdgptg56f5evch02n9t4@group.calendar.google.com'
    }
  });
  calendar.render();
};
function ShowCalendar4() {
  var calendarEl = document.getElementById('calendar4');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    googleCalendarApiKey: 'AIzaSyBvT8Tqbh0ygPsWTylTiE0MejzwDsr9bQU',
    events: {
      googleCalendarId: '28ssr4sdgptg56f5evch02n9t4@group.calendar.google.com'
    }
  });
  calendar.render();
};
function ShowCalendar5() {
  var calendarEl = document.getElementById('calendar5');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    googleCalendarApiKey: 'AIzaSyBvT8Tqbh0ygPsWTylTiE0MejzwDsr9bQU',
    events: {
      googleCalendarId: '28ssr4sdgptg56f5evch02n9t4@group.calendar.google.com'
    }
  });
  calendar.render();
};
function ShowCalendar6() {
  var calendarEl = document.getElementById('calendar6');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    googleCalendarApiKey: 'AIzaSyBvT8Tqbh0ygPsWTylTiE0MejzwDsr9bQU',
    events: {
      googleCalendarId: '28ssr4sdgptg56f5evch02n9t4@group.calendar.google.com'
    }
  });
  calendar.render();
};

document.addEventListener('DOMContentLoaded', function(){
  let cd = new Date().toISOString().slice(0, 10)
  let fd = new Date()
  fd.setMonth( fd.getMonth() + 1 );
  fd = fd.toISOString().slice(0,10)
  const txtCal = document.getElementById('test')
  txtCal.setAttribute('max', fd)
  txtCal.setAttribute('min', cd)
});
