//  Created by Stepan on 21/07/16.

import Foundation

let fileManager = NSFileManager()

let parsedData = FastaParser.parse("/Users/admin/GoTo/Bio/progress/Stepan/X2/reads.fa")

let result = GCCTrainer.train(parsedData["O"]!, degree: 25)

guard let json = try? NSJSONSerialization.dataWithJSONObject(result, options: []) else {
    print ("json error")
    exit(228)
}
fileManager.createFileAtPath("/Users/admin/GoTo/Bio/progress/Stepan/X2/GCHist.json", contents: json, attributes: [:])
print ("  end")
//посчитать гц контент а потом искать штуки