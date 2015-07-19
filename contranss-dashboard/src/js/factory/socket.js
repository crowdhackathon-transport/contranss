angular.module('Dashboard').factory('Socket', function($rootScope) {
    var service = {};
    var client = {};

    service.connect = function(host, port, user, password) {
        var options = {
            username: user,
            password: password
        };
        console.log("Try to connect to MQTT Broker " + host + " with user " + user);
        client = mqtt.connect('ws://' + host + ':' + port);

        client.on('error', function(err) {
            console.log('error!', err);
            client.stream.end();
        });
    };

    service.subscribe = function(topic) {
        client.subscribe(topic);
        console.log('subscribe ' + topic);
        client.on('error', function(err) {
            console.log('error!', err);
            client.stream.end();
        });
        client.on('message', function(topic, message) {
            service.callback(topic, message);
        });
    };

    service.publish = function(topic, payload) {
        client.publish(topic, payload, {
            retain: true
        });
        console.log('publish-Event sent ' + payload + ' with topic: ' + topic + ' ' + client);
    };
    service.onMessage = function(callback) {
        service.callback = callback;
    };
    return service;
});