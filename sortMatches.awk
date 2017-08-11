BEGIN{

    FS = "\n"
    OFS = "|"

    prez["Obama"] 
    prez["Bush2"]
    prez["Clinton"]
    prez["Bush"] 
    prez["Reagan"]

    for (p in prez){
            system("less matches_" p "|sort|uniq -c| sort -b -n -r >sortedMatches_" p)
}
}

