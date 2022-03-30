#!/usr/bin/python

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
    wifi_prepped = False
    attack_started = False

    def __init__(self):
        super().__init__(title="Wifite2 UI")
        self.set_border_width( 10 )

        hbox = Gtk.Box( spacing=6 )
        self.add(hbox)

        button = Gtk.Button.new_with_label( "Prepare Wifi Card" )
        button.connect( "clicked", self.btnPrepare )
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic( "Start Attack" )
        button.connect( "clicked", self.btnStart )
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic( "_Close" )
        button.connect( "clicked", self.btnClose )
        hbox.pack_start(button, True, True, 0)

    def btnPrepare(self, button):
        if self.wifi_prepped:
            button.set_label( "Wifi ReNormalized" )
        else:
            button.set_label("Wifi Prepped")
        self.wifi_prepped = not self.wifi_prepped

    def btnStart(self, button):
        if self.attack_started:
            button.set_label( "Attacking..." )
        else:
            button.set_label("Stop Attack")
        self.wifi_prepped = not self.wifi_prepped

    def btnClose(self, button):
        Gtk.main_quit()


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()