# Building Your First SSRS Report - Pluralsight

## Formatting Reports

### Address Page Size

1. Click in whitespace out of report to open Report Properties
   - Ensure `InteractiveSize` is page size
   - Change Left and Right `Margins` to .5
2. Click white space in report to open Body Propoerties
   - Change Size --> Width relative to the margin
        - Example: 8.5in x 11in with .5 margin on sides, width = 7.5in  
    - Height does not need to be edited because report will take up the amount of paper avaiable
3. To keep column headers throughout report:
    - Column Groups --> Advanced
    - Select first (Static) in Row Groups
    - Change `KeepWithGroup` to `After` and `RepeatOnNewPage` to `True`
    - To add page header
        - Right click empty space and click `Add Page Header`
4.  It is a good idea to have user information and date report was run in footer
    - Add Footer
    - Text box
    - Expression
