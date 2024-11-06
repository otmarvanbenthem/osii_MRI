# Contributing to _OSII Mini_ ultraLow Field MRI project 

:tada::balloon::cake: **Welcome to _OSII mini_ repository!** :cake::balloon::tada:

:dizzy::hatched_chick::sunny: _We're excited that you're here and want to contribute._ :sunny::hatched_chick::dizzy:

We want to ensure that every user and contributor feels welcome, included and supported to participate in this project.
We hope that the information provided in this document will make it as easy as possible for you to get involved.

We welcome all contributions to this project via GitHub issues and pull requests.
Please follow these guidelines to make sure your contributions can be easily integrated into the projects.

If you have any questions that aren't discussed below, please let us know through one of the many ways to [get in touch](#get-in-touch).

## Table of contents

Been here before? Already know what you're looking for in this guide? Jump to the following sections:

- [Get in touch](#get-in-touch)
- [Contributing through GitHub](#contributing-through-github)
- [Writing in Markdown](#writing-in-markdown)
- [Where to start: issues](#where-to-start-issues)
  - [Issue labels](#issue-labels)
- [Making a change with a pull request](#making-a-change-with-a-pull-request)
  - [1. Comment on an existing issue or open a new issue referencing your addition](#1-comment-on-an-existing-issue-or-open-a-new-issue-referencing-your-addition)
  - [2. Fork _The Turing Way_ repository to your profile](#2-forkgithub-fork-the-turing-way-repositoryturing-way-repo-to-your-profile)
  - [3. Make the changes you've discussed](#3-make-the-changes-youve-discussed)
  - [4. Submit a pull request](#4-submit-a-pull-requestgithub-pullrequest)
- [Style Guide](#style-guide)
- [Recognising Contributions](#recognising-contributions)


## Get in touch

Here we'll add multiple ways to get in touch with _OSII mini_ team!


## Contributing through GitHub

[Git][git] is a really useful tool for version control. 
[GitHub][github] sits on top of Git and supports collaborative and distributed working.

We know that it can be daunting to start using Git and GitHub if you haven't worked with them in the past, but _The Turing Way_ maintainers are here to help you figure out any of the jargon or confusing instructions you encounter! :heart:

In order to contribute via GitHub, you'll need to set up a free account and sign in.
Here are some [instructions](https://help.github.com/articles/signing-up-for-a-new-github-account/) to help you get going.
Remember that you can ask us any questions you need to along the way.

## Writing in Markdown

GitHub has a helpful page on [getting started with writing and formatting on GitHub](https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github).

Most of the writing that you'll do will be in [Markdown][markdown].
You can think of Markdown as a few little symbols around your text that will allow GitHub to render the text with a little bit of formatting.
For example, you could write words as **bold** (`**bold**`), or in _italics_ (`_italics_`), or as a [link][rick-roll] (`[link](https://youtu.be/dQw4w9WgXcQ)`) to another webpage.

Also when writing in Markdown, please [start each new sentence on a new line](https://the-turing-way.netlify.app/community-handbook/style.html#write-each-sentence-in-a-new-line-line-breaks).
Having each sentence on a new line will make no difference to how the text is displayed, there will still be paragraphs, but it makes the [diffs produced during the pull request](https://help.github.com/en/articles/about-comparing-branches-in-pull-requests) review easier to read! :sparkles:


## Where to start: issues

Before you open a new issue, please check if any of our [open issues](./issues) cover your idea already.
If you open a new issue, please follow our basic guidelines laid out in our [issue templates]().

### Issue labels

The list of labels for current issues can be found [here][turing-way-labels] and includes:

- [![approval-request](https://img.shields.io/badge/-approval%20request-8bd82d.svg)][labels-approval-request] _When a bug or minor changes have been made, contributors can label their PR along with "bug fixed"._

- [![Bug](https://img.shields.io/badge/-bug-d73a4a.svg)][labels-bug] _These issues are reporting a problem or a mistake in the project._

  The more details you can provide the better!
  If you know how to fix the bug, please open an issue first and then submit a pull request :sparkles:

- [![bug-fixed](https://img.shields.io/badge/-bug%20fixed-cef298.svg)][labels-bug-fixed] _These are bugs that have been fixed and only need approval._

  This is all about collaborating, so please let us know how we can best support you as a community member.

- [![conflicting-file-error](https://img.shields.io/badge/-conflicting--file--error-a00819.svg)][labels-conflicting-file-error] _These issues mark issues and pull requests with conflicting files and errors._

- [![dependencies](https://img.shields.io/badge/-dependencies-0366d6.svg)][labels-dependencies] _These issues relate to pull requests that update a dependency file._

- [![Enhancement](https://img.shields.io/badge/-enhancement-84b6eb.svg)][labels-enhancement] _These issues are suggesting new features that can be added to the project._

  If you want to ask for something new, please try to make sure that your request is distinct from any others that are already in the queue (or part of _The Turing Way_).
  If you find one that's similar but there are subtle differences please reference the other enhancement in your issue.

- [![good-first-issue](https://img.shields.io/badge/-good%20first%20issue-1b3487.svg)][labels-firstissue] _These issues are particularly appropriate if it is your first contribution to _OSII mini_

  If you're not sure about how to go about contributing, these are good places to start. You'll be mentored through the process by the maintainers team.
  If you're a seasoned contributor, please select a different issue to work from and keep these available for the newer and potentially more anxious team members.

- [![help-wanted](https://img.shields.io/badge/-help%20wanted-159818.svg)][labels-helpwanted] _These issues contain a task that a member of the team has determined we need additional help with._

  If you feel that you can contribute to one of these issues, we especially encourage you to do so!

- [![idea-for-discussion](https://img.shields.io/badge/-idea--for--discussion-a2f29b.svg)][labels-idea-for-discussion] _These issues can be used for inviting discussion from collaborators or community in general._

- [![newsletter](https://img.shields.io/badge/-newsletter-81e2c4.svg)][labels-newsletter] _These issues contain items that can be added to the newsletter._

- [![outreach](https://img.shields.io/badge/-Outreach-fcbae8.svg)][labels-outreach] _These issues relate to topics to reach out to the community._

- [![good-first-PR-review](https://img.shields.io/badge/-good--first--PR--review-C992E0.svg)][labels-good-first-PR-review] _These pull requests are for the new members of _The Turing Way_ community who want to start with reviewing and approving some simple pull requests._

If you are a new member of _OSII mini_ and are looking for opportunities to start as a reviewer of contributions made on our Github repository, these pull requests are a great starting point for you. Issues like small modifications, typo errors and minor bug fixes are resolved by these PRs which are easy to review as a beginner.

- [![pr-draft](https://img.shields.io/badge/-PR%3A%20draft-6a737d.svg)][labels-pr-draft] _These issues relate to draft pull requests._

- [![pr-merged](https://img.shields.io/badge/-PR%3A%20merged-6f42c1.svg)][labels-pr-merged] _These issues relate to pull requests that have been merged._

- [![pr-partially-approved](https://img.shields.io/badge/-PR%3A%20partially--approved-7E9C82.svg)][labels-pr-partially-approved] _These issues relate to pull requests that have been partially approved._

- [![pr-reviewed-approved](https://img.shields.io/badge/-PR%3A%20reviewed--approved-0e8a16.svg)][labels-pr-reviewed-approved] _These issues relate to pull requests that have been approved by a reviewer._

- [![pr-reviewed-changes-requested](https://img.shields.io/badge/-PR%3A%20reviewed--changes--requested-c2e0c6.svg)][labels-pr-reviewed-changes-requested] _These issues relate tp pull requests for which a reviewer has requested changes._

- [![pr-unreviewed](https://img.shields.io/badge/-PR%3A%20unreviewed-fbca04.svg)][labels-pr-unreviewed] _These issues relate to pull requests that have not been reviewed yet._

- [![question](https://img.shields.io/badge/-question-cc317c.svg)][labels-question] _These issues contain a question that you'd like to have answered._

  There are [lots of ways to ask questions](#get-in-touch) but opening an issue is a great way to start a conversation and get your answer.

- [![ready-for-merge](https://img.shields.io/badge/-ready%20for%20merge-32a320.svg)][labels-ready-for-merge] _These issues can be used after approving a pull request to let the author know that they can merge it._

- [![review-request](https://img.shields.io/badge/-review%20request-ed0602.svg)][labels-review-request] _These relate to pull requests for urgent review requests, for example, to approve a report, abstract, and newsletter._

- [![software-skills](https://img.shields.io/badge/-software--skills-ed886f.svg)][labels-software-skills] _These relate to issues and pull requests that may need some software development, design, or troubleshooting skills._

- [![typo-fix](https://img.shields.io/badge/-typo--fix-ff54d4.svg)][labels-typo-fix] _These issues relate to fixing typos and broken links._

- [![work-in-progress](https://img.shields.io/badge/-work--in--progress-e08f72.svg)][labels-work-in-progress] _These issues are work in progress._

## Making a change with a pull request

We appreciate all contributions to _OSII mini_.
**THANK YOU** for helping us build this useful resource. :sparkles::star2::dizzy:

All project management, conversations and questions related to _OSII mini_ project happens here.

The following steps are a guide to help you contribute in a way that will be easy for everyone to review and accept with ease :sunglasses:.

### 1. Comment on an [existing issue](./issues) or open a new issue referencing your addition

This allows other members of _OSII mini_ developers team to confirm that you aren't overlapping with work that's currently underway and that everyone is on the same page with the goal of the work you're going to carry out.

[This blog](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) is a nice explanation of why putting this work in upfront is so useful to everyone involved.

Remember, if you open a new issue, please follow our basic guidelines laid out in our [issue template]().
The issue template will automatically be rendered in the comment section of the new issue page so all you need to do is edit the "_Lorem ipsum_" sections.

### 2. [Fork][github-fork] this repository
This is now your own unique copy of _OSII mini_.
Changes here won't affect anyone else's work, so it's a safe space to explore edits to the code!

Make sure to [keep your fork up to date][github-syncfork] with the master repository, otherwise, you can end up with lots of dreaded [merge conflicts][github-mergeconflicts].

### 3. Make the changes you've discussed

Try to keep the changes focused.
If you submit a large amount of work all in one go it will be much more work for whoever is reviewing your pull request.

While making your changes, commit often and write good, detailed commit messages.
[This blog](https://chris.beams.io/posts/git-commit/) explains how to write a good Git commit message and why it matters.
It is also perfectly fine to have a lot of commits - including ones that break code.

Are you new to Git and GitHub or just want a detailed guide on getting started with version control? Check out our [Version Control chapter](https://the-turing-way.netlify.com/version_control/version_control.html) in _The Turing Way_ Book!

### 4. Submit a [pull request][github-pullrequest]

We encourage you to open a pull request as early in your contributing process as possible.
This allows everyone to see what is currently being worked on.
It also provides you, the contributor, feedback in real-time from both the community and the continuous integration as you make commits (which will help prevent stuff from breaking).

When you are ready to submit a pull request, you will automatically see the [Pull Request Template]() contents in the pull request body.
It asks you to:

- Describe the problem you're trying to fix in the pull request, reference any related issue and use fixes/close to automatically close them, if pertinent.
- List of changes proposed in the pull request.
- Describe what the reviewer should concentrate their feedback on.

By filling out the "_Lorem ipsum_" sections of the pull request template with as much detail as possible, you will make it really easy for someone to review your contribution!

If you have opened the pull request early and know that its contents are not ready for review or to be merged, add "[WIP]" at the start of the pull request title, which stands for "Work in Progress".
When you are happy with it and are happy for it to be merged into the main repository, change the "[WIP]" in the title of the pull request to "[Ready for review]".

A member of _OSII mini_ developers team will then review your changes to confirm that they can be merged into the main repository.
A [review][github-review] will probably consist of a few questions to help clarify the work you've done.
Keep an eye on your GitHub notifications and be prepared to join in that conversation.

You can update your [fork][github-fork] of _The Turing Way_ [repository][turing-way-repo] and the pull request will automatically update with those changes.
You don't need to submit a new pull request when you make a change in response to a review.

You can also submit pull requests to other contributors' branches!
Do you see an [open pull request](https://github.com/alan-turing-institute/the-turing-way/pulls) that you find interesting and want to contribute to?
Simply make your edits on their files and open a pull request to their branch!

What happens if the continuous integration (CI) fails (for example, if the pull request notifies you that "Some checks were not successful")?
The CI could fail for a number of reasons.
At the bottom of the pull request, where it says whether your build passed or failed, you can click “Details” next to the test, which takes you to the Travis page.
If you have the write access to the repo, you can view the log or rerun the checks by clicking the “Restart build” button in the top right.
Please note that you need to be logged in to Travis CI with your GitHub account see the “Restart build” button.
You can learn more about Travis in the [Continuous Integration chapter](https://the-turing-way.netlify.com/continuous_integration/continuous_integration.html) of the book!

GitHub has a [nice introduction][github-flow] to the pull request workflow, but please [get in touch](#get-in-touch) if you have any questions :balloon:.

## Recognising Contributions

We welcome and recognise all kinds of contributions, from fixing small errors, to developing documentation, maintaining the project infrastructure, writing chapters or reviewing existing resources.

You can see the [Emoji Key (Contribution Types Reference)](https://allcontributors.org/docs/en/emoji-key) for a list of valid `<contribution>` types.

---

_These Contributing Guidelines have been adapted from [the Turing Way](https://github.com/alan-turing-institute/the-turing-way/), which in turn are adopted from the [Contributing Guidelines](https://github.com/bids-standard/bids-starter-kit/blob/master/CONTRIBUTING.md) of the [BIDS Starter Kit](https://github.com/bids-standard/bids-starter-kit)! (License: CC-BY)_

[git]: https://git-scm.com
[github]: https://github.com
[github-branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[github-fork]: https://help.github.com/articles/fork-a-repo
[github-flow]: https://guides.github.com/introduction/flow
[github-mergeconflicts]: https://help.github.com/articles/about-merge-conflicts
[github-pullrequest]: https://help.github.com/articles/creating-a-pull-request
[github-review]: https://help.github.com/articles/about-pull-request-reviews
[github-syncfork]: https://help.github.com/articles/syncing-a-fork
[issue-template]: ISSUE_TEMPLATE.md
[labels-link]: https://github.com/alan-turing-institute/the-turing-way/labels
[labels-bug]: https://github.com/alan-turing-institute/the-turing-way/labels/bug
[labels-bug-fixed]: https://github.com/alan-turing-institute/the-turing-way/labels/bug%20fixed
[labels-collaboration-book]: https://github.com/alan-turing-institute/the-turing-way/labels/collaboration%2Dbook
[labels-communication-book]: https://github.com/alan-turing-institute/the-turing-way/labels/communication%2Dbook
[labels-community]: https://github.com/alan-turing-institute/the-turing-way/labels/community
[labels-comms]: https://github.com/alan-turing-institute/the-turing-way/labels/comms
[labels-conflicting-file-error]: https://github.com/alan-turing-institute/the-turing-way/labels/conflicting%2Dfile%2Derror
[labels-dependencies]: https://github.com/alan-turing-institute/the-turing-way/labels/dependencies
[labels-enhancement]: https://github.com/alan-turing-institute/the-turing-way/labels/enhancement
[labels-ethics-book]: https://github.com/alan-turing-institute/the-turing-way/labels/ethics%2Dbook
[labels-events]: https://github.com/alan-turing-institute/the-turing-way/labels/events
[labels-firstissue]: https://github.com/alan-turing-institute/the-turing-way/labels/good%20first%20issue
[labels-helpwanted]: https://github.com/alan-turing-institute/the-turing-way/labels/help%20wanted
[labels-idea-for-discussion]: https://github.com/alan-turing-institute/the-turing-way/labels/idea%2Dfor%2Ddiscussion
[labels-good-first-PR-review]: https://github.com/alan-turing-institute/the-turing-way/labels/good%2Dfirst%2PR%2review
[labels-jupyter]: https://github.com/alan-turing-institute/the-turing-way/labels/jupyter
[labels-project-management]: https://github.com/alan-turing-institute/the-turing-way/labels/project%20management
[labels-newsletter]: https://github.com/alan-turing-institute/the-turing-way/labels/newsletter
[labels-outreach]: https://github.com/alan-turing-institute/the-turing-way/labels/Outreach
[labels-pr-draft]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20draft
[labels-pr-merged]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20merged
[labels-pr-partially-approved]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20partially%2Dapproved
[labels-pr-reviewed-approved]: https://github.com/alan-turing-institute/the-turing-way/labels/PR%3A%20reviewed%2Dapproved
[labels-question]: https://github.com/alan-turing-institute/the-turing-way/labels/question
[labels-ready-for-merge]: https://github.com/alan-turing-institute/the-turing-way/labels/ready%20for%20merge
[labels-tools]: https://github.com/alan-turing-institute/the-turing-way/labels/tools
[labels-typo-fix]: https://github.com/alan-turing-institute/the-turing-way/labels/typo%2Dfix
[labels-work-in-progress]: https://github.com/alan-turing-institute/the-turing-way/labels/work%2Din%2Dprogress
[labels-workshops]: https://github.com/alan-turing-institute/the-turing-way/labels/workshops
[markdown]: https://daringfireball.net/projects/markdown

