Sub stocks():

Dim Total_volume As Double

Dim closing_price As Double

Dim opening_price As Double

Dim Difference As Double

Dim percentage_change1 As Double

Dim percentage_change2 As String

Dim stock_name As String

Dim results As Long

Dim Last_row As Long

Dim Last_row2 As Long

Dim ws As Worksheet


'Iterate through sheets'
For Each ws In Sheets

ws.Cells(1, 9).Value = "Ticker"
ws.Cells(1, 10).Value = "Total Stock Volume"
ws.Cells(1, 11).Value = "Yearly Change"
ws.Cells(1, 12).Value = "Percentage Change"
ws.Cells(2, 15).Value = "Greatest % Increase"
ws.Cells(3, 15).Value = "Greatest % Decrease"
ws.Cells(4, 15).Value = "Greatest Total Volume"
ws.Cells(1, 16).Value = "Ticker"
ws.Cells(1, 17).Value = "Value"

'Get the last Row on the work Sheet'
Last_row = ws.Cells(Rows.Count, 1).End(xlUp).Row


'Assighn opening Price'
opening_price = ws.Cells(2, 3)

'Initialize total volume'
Total_volume = 0

'location where you want the results to show up'
results = 2

    For i = 2 To Last_row

        'IF LAST ROW OF A GROUP'
        If ws.Cells(i, 1) <> ws.Cells(i + 1, 1) Then
        
        'Get closing Price'
        closing_price = ws.Cells(i, 6).Value
        
        'calculate the difference'
        Difference = closing_price - opening_price
        
        'calculate percentage change'
        percentage_change = (Difference) / (opening_price)
        
        'convert to percentage'
        percentage_change2 = FormatPercent(percentage_change)
        
        'Store the Stock name'
        stock_name = ws.Cells(i, 1).Value
        
        'Get the total volume, if it is the last row'
        Total_volume = Total_volume + ws.Cells(i, 7).Value
        
        'output the stock name'
        ws.Range("I" & results).Value = stock_name
        
        'output total volume'
        ws.Range("J" & results).Value = Total_volume
        
        'output diffrence'
        ws.Range("K" & results).Value = Difference
        
        'output percentage_change2'
        ws.Range("L" & results).Value = percentage_change2
        
        'Move the next stocks output to next row'
        results = results + 1
        
        'Reset total volume back to zero'
        Total_volume = 0
        
        'Reset opening Price'
        
        'If opening price is 0, find non-zero opening price'
        While ws.Cells(i + 1, 3) = 0 And i < Last_row
            i = i + 1
        Wend
        
        'if opening price is non-zero'
        opening_price = ws.Cells(i + 1, 3)
        
        'IF NOT IN LAST ROW OF A GROUP'
        Else
        
        'Getting cumilative total of Volume'
        Total_volume = Total_volume + ws.Cells(i, 7).Value


        End If

    Next i
    
    ' SETTING CELL COLOUR FORMAT AND ALSO GET GREATEST %inc, %dec and Tot vol'
    
    'Get the last Row from results'
    Last_row2 = ws.Cells(Rows.Count, 9).End(xlUp).Row
    
    Dim MaxPercentInc As Double
    Dim MaxPercentDec As Double
    Dim MaxTotalVol As Double
    
    MaxPercentInc = 0
    MaxPercentDec = 0
    MaxTotalVol = 0
    
    Dim maxPercIncIndex As Long
    Dim maxPercDecIndex As Long
    Dim maxTotalVolndex As Long
    
    For j = 2 To Last_row2
    
        If ws.Cells(j, 11).Value < 0 Then
        ws.Cells(j, 11).Interior.ColorIndex = 3
        
        ElseIf ws.Cells(j, 11).Value > 0 Then
        ws.Cells(j, 11).Interior.ColorIndex = 4
        
        End If
        
    'Get greatest percent increase and greatest percent decrease and greatest total volume'
    
        
       'Get the index for the stock name with greatest percent increase'
        If ws.Cells(j, 12) > MaxPercentInc Then
            'Reset Maxperinc to the new highest'
            MaxPercentInc = ws.Cells(j, 12)
            'Store the index value'
            maxPercIncIndex = j
        End If
        
        'Get the index for the stock name with greatest percent decrease'
        If ws.Cells(j, 12) < MaxPercentDec Then
            MaxPercentDec = ws.Cells(j, 12)
            maxPercDecIndex = j
        End If
    
    'Get the index for the stock name with greatest total volume'
     If ws.Cells(j, 10) > MaxTotalVol Then
            MaxTotalVol = ws.Cells(j, 10)
            maxTotalVolndex = j
        End If
    
    Next j
    
    'Output Stock Name and the Greatest Percentage increase'
    ws.Cells(2, 16) = ws.Cells(maxPercIncIndex, 9)
    ws.Cells(2, 17) = ws.Cells(maxPercIncIndex, 12)
    ws.Cells(2, 17) = FormatPercent(ws.Cells(2, 17), 2)
    
    'Output Stock Name and the Greatest Percentage Decrease'
    ws.Cells(3, 16) = ws.Cells(maxPercDecIndex, 9)
    ws.Cells(3, 17) = ws.Cells(maxPercDecIndex, 12)
    ws.Cells(3, 17) = FormatPercent(ws.Cells(3, 17), 2)
    
    'Output Stock Name and the Greatest Total Volume'
    ws.Cells(4, 16) = ws.Cells(maxTotalVolndex, 9)
    ws.Cells(4, 17) = ws.Cells(maxTotalVolndex, 10)
    
Next ws
    
End Sub


