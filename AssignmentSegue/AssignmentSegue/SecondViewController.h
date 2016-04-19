//
//  SecondViewController.h
//  AssignmentSegue
//
//  Created by Devashish Badlani on 4/15/16.
//  Copyright © 2016 Devashish Badlani. All rights reserved.
//

#import <UIKit/UIKit.h>



@interface SecondViewController : UIViewController<UITextFieldDelegate>
@property (weak, nonatomic) IBOutlet UILabel *displayLabel2;

@property (strong,nonatomic) NSString *stringFromTextField1;


@end
