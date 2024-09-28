USE OLYMPICS_DB
GO

CREATE OR ALTER PROC CREATESQLSERVERLESSVIEW_GOLD @VIEWNAME NVARCHAR(100)
AS
BEGIN

    DECLARE @STATEMENT NVARCHAR(MAX)

    SET @STATEMENT = N'CREATE OR ALTER VIEW ' + @VIEWNAME + ' AS 
    SELECT *
    FROM OPENROWSET(
            BULK ''https://dlgen2migproject1.dfs.core.windows.net/gold/dbo/' + @VIEWNAME + '/'',
            FORMAT = ''DELTA''
        ) AS [result];'
    
    -- Use sp_executesql to execute the dynamic SQL statement
    EXEC sp_executesql @STATEMENT

END
GO
