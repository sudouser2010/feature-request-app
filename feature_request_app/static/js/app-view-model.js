

function OptionItem(name, id, disable){
    var self = this;

    self.id = ko.observable(id);
    self.name = ko.observable(name);
    self.disabled = ko.observable(disable);
};

function FeedbackModal(){
    var self = this;

    self.modal = "#feedback-modal";
    self.title=ko.observable("");
    self.message=ko.observable("");

	self.showModal = function(){
		$(self.modal).modal('show');
	};
	self.closeModal = function(){
		$(self.modal).modal('hide');
	};

    self.showSuccess = function(){
        self.title("New Feature Request Created !");
        self.message("");
    };
    self.showFailure = function(){
        self.title("Invalid Input");
        self.message("");
    };

};

function AppViewModel(){
    var self = this;

    self.title=ko.observable("");
    self.description=ko.observable("");
    self.selectedClient=ko.observable(-1);
    self.priority=ko.observable("");
    self.date=ko.observable("");
    self.url=ko.observable("");
    self.selectedArea=ko.observable(-1);

    self.clients = [
        new OptionItem( 'Select Client', -1, true),
        new OptionItem( 'A', 0, false),
        new OptionItem( 'B', 1, false),
        new OptionItem( 'C', 2, false),
    ];
    self.productArea = [
        new OptionItem( 'Select Product Area', -1, true),
        new OptionItem( 'Policies', 0, false),
        new OptionItem( 'Billing', 1, false),
        new OptionItem( 'Claims', 2, false),
        new OptionItem( 'Reports', 3, false),
    ];
    self.setOptionAsDisabled = function(option, item) {
        ko.applyBindingsToNode(option, {disable: item.disabled}, item);
    };

    self.feedbackModal = new FeedbackModal();

    self.createFeatureRequest = function(){
        var newClientData = {
            'title' : self.title(),
            'description' : self.description(),
            'client' : self.selectedClient(),
            'priority' : parseInt(self.priority()),
            'target_date' : self.date(),
            'ticket_url' : self.url(),
            'product_area' : self.selectedArea(),
        };

		var options = {
			type: "POST",
			url: document.location.origin + "/api/feature-requests/",
			timeout: 700,
			data: newClientData
		};

		$.ajax(options).done(function(result) {
            console.log("done");
            self.feedbackModal.showSuccess();
            self.feedbackModal.showModal();
		}).fail(function(result) {
            console.log("fail");
            self.feedbackModal.showFailure();
            self.feedbackModal.showModal();
		})

    }
};

var vm = new AppViewModel();
ko.applyBindings(vm);
