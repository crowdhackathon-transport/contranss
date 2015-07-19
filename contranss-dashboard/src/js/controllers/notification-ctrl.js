angular.module('Dashboard').controller('NotificationCtrl', ['Status', '$timeout', NotificationCtrl]);

function NotificationCtrl(Status, $timeout) {
    var vm = this;

    function info() {
        swal({
            title: "HTML <small>Title</small>!",
            text: 'A custom <span style="color:#F8BB86">html<span> message.',
            html: true
        });
    }
    vm.info = info;

    function callAtTimeout() {
        var notifications = [];
        Status.get({}, function(status) {
            status.hits.forEach(function(item) {
                notifications.push(item._source);
            });
        });
        vm.notifications = notifications;
        console.log('lol');
    }
    callAtTimeout();
    $timeout(callAtTimeout, 5000);
}