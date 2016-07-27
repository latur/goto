//  Created by Stepan on 19/07/16.

import Foundation

class GCContentTrainer {
    static func train(parsedData: [String: [String]]) -> NSData {
        var histogramData: [String: [String: String]] = ["E": [:], "C": [:]]
        
        //GCContent calculation here
        createHistogram("E", parsedData: parsedData, histoData: &histogramData)
        createHistogram("C", parsedData: parsedData, histoData: &histogramData)
        
        //JSON creation
        guard let json = try? NSJSONSerialization.dataWithJSONObject(histogramData, options: []) else {
            print ("NSJSONSer Error")
            exit(228)
        }
        
        return json
    }
    
    private static func createHistogram (name: String, parsedData: [String: [String]], inout histoData: [String: [String: String]]) {
        var percentage = ""
        for read in parsedData[name]! {
            percentage = String(Int(GCContentCalc.calculate(read)*100))
            if histoData[name]![percentage] == nil {
                histoData[name]![percentage] = "0"
            }
            
            //TODO: убрать эти названия
            let SHHHHIIIIET = histoData[name]![percentage]!
            let DERRRRMMOOO = Int(SHHHHIIIIET)!+1
            
            histoData[name]![percentage]! = "\(DERRRRMMOOO)"//+= "\((Int(histoData[name]![percentage]!)!+1))"
        }
        print ("  GCContent calculated for \(name) object")
    }
}
