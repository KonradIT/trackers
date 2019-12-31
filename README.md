## What is this

- A comprehensive list of companies that track your location, phone usage, and other data via your smartphone.
- A tool to generate a block list.
- Block lists ready to use

Note, most of the tools are designed to be used against an Android phone.

## Why?

Recently, The Times got access to a CSV file containing location pings collected by a location tracking company. If you do not want a location company or a journalist to track you via the apps you use follow this.

## Sources:

- https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-cell-phone.html
- https://mightysignal.com/sdk-directory/android
- Exodus app on my phone

## How to apply a blocklist:

- Download and install DNS66: https://f-droid.org/en/packages/org.jak_linux.dns66/
- On this repo, go to 'blocklists' directory and pick one.
- Click the Raw button. Copy the URL.
- On DNS66, go to Hosts, click the blue FAB, add the URL you copied.

Then start it. DNS66 will block the URLs inside the blocklist.

## Then what?

This will not stop apps from gathering your data, it will stop them from sending it back home - in most cases. New York Times and other articles have detailed how to stop the data collection all-together (https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-privacy-tips.html). Mind you, these tips will generally restrict apps from gathering location using the Location permission, not using, for instance, Bluetooth scanning or WiFi scanning, which in my case it was possible to disable: https://twitter.com/konrad_it/status/1210140683769647104
