## OBJECTIVE
Write a shell script to create a quick workflow for creating a timestamped devlog entry.


## BACKGROUNDS AND ASSUMPTIONS
A timestamped devlog entry follows the format;
```
2022-12-09T00:00
This is a dev log entry.

It is a multi-line content that supports the markdown syntax.
```

Currently, each devlog entry is created manually through the following steps;
1. Open devlog.md using our editor
   In our case, we run the command `nvim devlog.md`
2. Move the cursor to the end of the file
   Initially, we scroll down to the end of the file. But we have since learnt to use `GA` to quickly move the cursor to the end of the last line and switch to insert mode.
3. Ensure a linebreak exists.
   We have to ensure that each devlog entry is clearly separated.
4. Type out the timestamp manually
   Initially, we type the timestamp manually. But we have since that we can run `:r !date` within nvim to insert the date in the next line. 
5. Write out the content of the entry.
6. Save the changes and exit.


## FEATURES / USER STORIES
- User should be able to write and edit devlog entries in an isolated buffer.
- Script should insert the timestamp of the devlog entry automatically at point of creation.
- A newly created devlog entry should be appended to the end of the devlog.md file.


## CONSTRAINTS AND DEPENDENCIES
This is a minimum-viable product and as such, we are keeping the complexity as low as possible. Some ideas that were came up but is not in scope includes;
- User should be able to configure whether entries are added at the start/end of file.
- User should be able to configure the date format for the timestamp.
- User should be able to use templates.

## OPEN QUESTIONS AND ADDITIONAL INFORMATION
[What is a good product requirements document document template](https://www.aha.io/roadmapping/guide/requirements-management/what-is-a-good-product-requirements-document-template)

Initially, we considered using gum from charm.sh to add some flair. But let's keep that out for now.
