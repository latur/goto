//  Created by Stepan on 19/07/16.

import Foundation



let fileManager = NSFileManager.defaultManager()

//Parsing
let parsedData = FastaParser.parse("/Users/admin/GoTo/Bio/progress/Stepan/train.fa")
print ("  Parsed data.\n")

//==========================
//GC content training
//==========================
//let json = GCContentTrain.trainer(parsedData)
//fileManager.createFileAtPath("/Users/admin/GoTo/Bio/progress/Stepan/GCtrain.json", contents: json, attributes: [:])
//print ("  Json created")
//==========================

//==========================
//FA training
//==========================
//let json = FrequencyAnalysisTrainer.train(parsedData)
//fileManager.createFileAtPath("/Users/admin/GoTo/Bio/progress/Stepan/FAtrain.json", contents: json, attributes: [:])
//print ("  Json created")
//==========================

//==========================
//MM training and testing
//==========================
let possibilities = MMTrainer.train(parsedData, degree: 9)

let testData = FastaParser.parse("/Users/admin/GoTo/Bio/progress/Stepan/test.fa")
print ("  Parsed test data.\n")

let result = MMTester.test(testData: testData, degree: 9, possibilities: possibilities)
fileManager.createFileAtPath("/Users/admin/GoTo/Btuyio/progress/Stepan/MMresult.txt", contents: (result as NSString).dataUsingEncoding(NSUTF8StringEncoding), attributes: [:])
print ("  Result is created.\n")
//==========================


//==========================
//GC content testing
//==========================
//let result = GCContentTester.test(testData)
//fileManager.createFileAtPath("/Users/admin/GoTo/Bio/progress/Stepan/GCresult.txt", contents: (result as NSString).dataUsingEncoding(NSUTF8StringEncoding), attributes: [:])
//print ("  Result is created.\n")
//==========================

//==========================
//FA testing
//==========================
//let result = FrequensyAnalysisTester.test(testData)
//fileManager.createFileAtPath("/Users/admin/GoTo/Bio/progress/Stepan/FAresult.txt", contents: (result as NSString).dataUsingEncoding(NSUTF8StringEncoding), attributes: [:])
//print ("  Result is created.\n")
//==========================


