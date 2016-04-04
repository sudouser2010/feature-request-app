

function OptionItem(name, id, disable){
    var self = this;

    self.id = ko.observable(id);
    self.name = ko.observable(name);
    self.disabled = ko.observable(disable);
};

function Client(title, desc, client, priority, date, url, area){
    var self = this;

    self.title = title;
    self.description = desc;
    self.client = client;
    self.priority = priority;
    self.targetDate = date;
    self.ticketURL = url;
    self.productArea = area;
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
    self.showFailure = function(response){
        self.title("Invalid Input");
        var message = self.renderMessage(response);
        self.message(message);
    };
    self.renderMessage = function(response){
        var messageHeader = "Please check the following fields: <br>";
        var messageErrors = [];

        for (var key in response){
          if (response.hasOwnProperty(key)) {
              messageErrors.push(key);
          }
        }
        return messageHeader + messageErrors.join(", ");
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

    self.api = document.location.origin + "/api/feature-requests/",
    self.clientData = ko.observableArray();

    self.resetFields = function(){
        self.title("");
        self.description("");
        self.selectedClient(-1);
        self.priority("");
        self.date("");
        self.url("");
        self.selectedArea(-1);
    };

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
    self.setOptionAsDisabled = function(option, item){
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
			url: self.api,
			timeout: 700,
			data: newClientData
		};

		$.ajax(options).done(function(result) {
            console.log("done");
            self.feedbackModal.showSuccess();
            self.feedbackModal.showModal();
            self.resetFields();
		}).fail(function(result) {
            console.log("fail");
            self.feedbackModal.showFailure(result.responseJSON);
            self.feedbackModal.showModal();
		})

    }

    self.getFeatureRequests = function(){

		var options = {
			type: "GET",
			url: self.api,
			timeout: 700,
		};

		$.ajax(options).done(function(result) {
            console.log("done");
            self.populateViewModel(result);
		}).fail(function(result) {
            console.log("fail");
		})

    };

    self.populateViewModel = function(result){
        /*
         * Use results from api to build observable of client data
         */
        for (var clientType in result){
            if (result.hasOwnProperty(clientType)){

                var clientTypeData = result[clientType];

                for (var clientDatum in clientTypeData){
                    if (clientTypeData.hasOwnProperty(clientDatum)){

                        var client = clientTypeData[clientDatum];
                        self.clientData.push(
                            new Client(
                                client.title,
                                client.description,
                                client.client,
                                client.priority,
                                client.target_date,
                                client.ticket_url,
                                client.product_area
                            )
                        );
                    }
                }
            }
        }
    };

    self.getFeatureRequests();
};

var vm = new AppViewModel();
ko.applyBindings(vm);
