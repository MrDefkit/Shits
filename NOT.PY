import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Test")

Notify.Notification.new("Hello").show()