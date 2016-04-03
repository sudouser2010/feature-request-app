
function OptionItem(name, id, disable) {
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
        new OptionItem( 'Select Client', 0, true),
        new OptionItem( 'A', 1, false),
        new OptionItem( 'B', 2, false),
        new OptionItem( 'C', 3, false),
    ];
    self.productArea = [
        new OptionItem( 'Select Product Area', 0, true),
        new OptionItem( 'Policies', 1, false),
        new OptionItem( 'Billing', 2, false),
        new OptionItem( 'Claims', 3, false),
        new OptionItem( 'Reports', 4, false),
    ];
    self.setOptionAsDisabled = function(option, item) {
        ko.applyBindingsToNode(option, {disable: item.disabled}, item);
    };
};

var vm = new AppViewModel();
ko.applyBindings(vm);
