//
//  ViewController.h
//  AssignmentSegue
//
//  Created by Devashish Badlani on 4/15/16.
//  Copyright © 2016 Devashish Badlani. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "SecondViewController.h"


@interface ViewController : UIViewController<UITextFieldDelegate>


@property (weak, nonatomic) IBOutlet UITextField *firstTextField;
- (IBAction)passTextToVC2Button:(id)sender;


@end

