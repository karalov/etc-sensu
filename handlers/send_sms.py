#!/opt/sensu/embedded/bin/ruby
require 'sensu-handler'
require 'rest-client'
class Show < Sensu::Handler
  def handle
    RestClient.post 'https://www.notifymydevice.com/push', {'ApiKey': settings['notify_my_device']['api_key'], 'PushTitle': @event['check']['name'], 'PushText': event_summary}
  end
end
