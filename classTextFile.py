class SubfieldsInAI():
    def Subfields(n,i):
        learning=['Sub-fields in AI are:','Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language         Processing']
        print(learning[i])
        if(n<=1):
            return n-1
        else:
            i = i + 1
            return SubfieldsInAI.Subfields(n-1,i)
class oddEven():
    def oddEven():
        num = int(input("Enter a number:"))
        if(num%2 == 0):
            print(num,' is Even number')
            message = num,' is Even number'
        else:
            print(num,' is Odd number')
            message = num,' is Odd number'
        return message
class ElegiblityForMarriage():
    def elegible(gender,age):
        if(age <= 20):
            print('Your Gender:',gender)
            print('Your Age:',age)
            print('NOT ELIGIBLE')
            message = gender ,age, 'NOT ELIGIBLE'
        else:
            print('Your Gender:',gender)
            print('Your Age:',age)
            print('ELIGIBLE')
            message = gender ,age, 'ELIGIBLE'
        return message
class FindPercent():
    def percentage(sub1,sub2,sub3,sub4,sub5):
        total = sub1+sub2+sub3+sub4+sub5
        percentage = total/500 * 100
        print('Subject1 =',sub1)
        print('Subject2 =',sub2)
        print('Subject3 =',sub3)
        print('Subject4 =',sub4)
        print('Subject5 =',sub5)
        print('Total:',total)
        print('Percentage:',percentage)
        per = percentage
        return per
class triangle():
    def triangel(height,breadth):
        areaFormula = (height*breadth)/2
        print('Area of Triangle:',areaFormula)
        return areaFormula
class permiter():
    def perimeter(height1,beight2,breadth):
         perimeterFormula = height1 + beight2 + breadth
         print('Perimeter of Triangle:',perimeterFormula)
         return perimeterFormula