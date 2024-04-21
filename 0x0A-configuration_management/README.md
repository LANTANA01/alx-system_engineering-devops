An Introduction to Configuration Management
Updated on May 17, 2019
Configuration Management
Getting Started
Conceptual
Default avatar
By Erika Heidi

Developer Advocate

English
An Introduction to Configuration Management
Introduction
As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.

Automation plays an essential role in server configuration management. It’s the mechanism used to make the server reach a desirable state, previously defined by provisioning scripts using a tool’s specific language and features. Automation is, in fact, the heart of configuration management for servers, and that’s why it’s common to also refer to configuration management tools as Automation Tools or IT Automation Tools.

Another common term used to describe the automation features implemented by configuration management tools is Server Orchestration or IT Orchestration, since these tools are typically capable of managing one to hundreds of servers from a central controller machine.

There are a number of configuration management tools available in the market. Puppet, Ansible, Chef and Salt are popular choices. Although each tool will have its own characteristics and work in slightly different ways, they are all driven by the same purpose: to make sure the system’s state matches the state described by your provisioning scripts.

Benefits of Configuration Management for Servers
Although the use of configuration management typically requires more initial planning and effort than manual system administration, all but the simplest of server infrastructures will be improved by the benefits that it provides. To name a few:

Quick Provisioning of New Servers
Whenever a new server needs to be deployed, a configuration management tool can automate most, if not all, of the provisioning process for you. Automation makes provisioning much quicker and more efficient because it allows tedious tasks to be performed faster and more accurately than any human could. Even with proper and thorough documentation, manually deploying a web server, for instance, could take hours compared to a few minutes with configuration management/automation.

Quick Recovery from Critical Events
With quick provisioning comes another benefit: quick recovery from critical events. When a server goes offline due to unknown circumstances, it might take several hours to properly audit the system and find out what really happened. In scenarios like this, deploying a replacement server is usually the safest way to get your services back online while a detailed inspection is done on the affected server. With configuration management and automation, this can be done in a quick and reliable way.

Requirements
General
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
Your Puppet manifests must run without error
Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
Your Puppet manifests files must end with the extension .pp
Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet


Puppet 5 Docs

Install puppet-lint
$ gem install puppet-lint
