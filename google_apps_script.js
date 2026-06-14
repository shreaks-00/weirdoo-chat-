function doPost(e) {
  try {
    // Open the active spreadsheet and select the first sheet
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Parse the JSON data sent from your website
    var data = JSON.parse(e.postData.contents);
    
    // Add the headers if the sheet is completely empty
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(["Timestamp", "Name", "Age", "Gender", "Country", "Avatar Emoji", "T&C Agreed"]);
      // Make headers bold
      sheet.getRange(1, 1, 1, 7).setFontWeight("bold"); 
    }
    
    // Append the new user's data to the next available row
    sheet.appendRow([
      data.timestamp || new Date(),
      data.name || "",
      data.age || "",
      data.gender || "",
      data.country || "",
      data.avatar || "",
      data.tnc || "FALSE"
    ]);
    
    // Return a success response
    return ContentService.createTextOutput(JSON.stringify({ "status": "success" }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch(error) {
    // Return an error response if something goes wrong
    return ContentService.createTextOutput(JSON.stringify({ "status": "error", "message": error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Keep a GET method just in case you ever want to check if the URL is alive in your browser
function doGet(e) {
  return ContentService.createTextOutput("WiredVibe Apps Script is running!");
}
