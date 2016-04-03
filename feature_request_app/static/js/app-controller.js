
function Client(name, id, disable) {
    var self = this;

    self.id = ko.observable(id);
    self.name = ko.observable(name);
    self.disabled = ko.observable(disable);
};

function AppViewModel() {
    var self = this;

    self.title=ko.observable("");
    self.description=ko.observable("");
    self.priority=ko.observable("");
    self.date=ko.observable("");
    self.url=ko.observable("");

    self.clients = [
        new Client( 'Select Client', 0, true),
        new Client( 'A', 1, false),
        new Client( 'B', 2, false),
        new Client( 'C', 3, false),
    ];
    self.setOptionAsDisabled = function(option, item) {
        ko.applyBindingsToNode(option, {disable: item.disable}, item);
    };
};

var vm = new AppViewModel();
ko.applyBindings(vm);
