# Chapter 2 - VEX Robotics Toolchain

This chapter is focused on getting started with Vex tools and programming VEX Robots

## Intro

VEX offers a variety of ways to program a Robot

1.  [VEXCode Blocks](https://www.vexrobotics.com/vexcode/blocks)
    - Simplest of the 3 options, but great for getting started with coding in VEX
    - Limited to the capability of Blocks already defined
    - Can be slow/difficult to read or write
    - Difficult to manage as a team for competition
2.  [VEXCode Text](https://www.vexrobotics.com/vexcode/text)
    - Slightly more complex than Blocks, but also great for getting started with drag and drop code snippets
    - Difficult to manage as a team for competition
3.  [VSCode Extension](https://www.vexrobotics.com/vexcode/vscode-extension)
    - Most advanced of the options, making it seem intimidating to get started
    - Most customization and capability with raw code access and additional VSCode Extensions to improve developer experience
    - Makes managing code across a team safer and more consistent with Git (Code Storage) integration

The VEX VSCode Extension is the preferred method for many teams because of its advanced capabilities and similarity to the rest of the Software Engineering industry. VEX has also deprecated VEXcode Pro in favor of the VSCode Extension going forward.

## Install and Setup

- [VSCode and VEX Extension Installation Guide](https://kb.vex.com/hc/en-us/articles/8608960771092-VS-Code-Installation-Guide-for-V5#installing-the-supporting-extensions-HInSe)

## Building Vex Software with VSCode

Once you have installed the VSCode extension, you should see the Vex icon on the left side of your window in the "Activity Bar". Click it to open the Vex extension. Now 3 sections should be visible:

1. Project Actions

   This is where we can start a new project from scratch, or open an existing project from somewhere in your files.

2. Vex Device Info

   This is where information from the Brain will be loaded if one is connected, either by USB or wirelessly through a USB connected controller. Details like Firmware version, ports, and device types will all be shown here

3. Vex Feedback

   This is installed by default and you can click the title bar to minimize it, we don't need it.

Let's start by creating a new Python project.

1. Click the "New Project" button to start the project startup gui.
2. Select "V5" as that is the platform we will be working with.
3. Select Python as the language.
4. Either select a template or the empty project template.
5. Enter a name and description for the project, both will be visible on the brain (both can be changed later if needed).
6. Choose a folder to save the project in.
7. Click "Create" to create the new project.

## Vex V5 API Documentation

The Vex Python documentation is available at - https://api.vex.com/v5/home/python/index.html#

This is a powerful resource detailing all of the Classes and Functions in the Vex Python library, with examples of how to use them.
